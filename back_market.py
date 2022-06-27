import json
import re
from datetime import datetime
from decimal import Decimal

from django.http import HttpResponse
from moneyouts.models import Moneyout
from payment import do_payout

DEFAULT_CURRENCY = "EUR"


def int_to_decimal(value):
    try:
        if len(str(value)) == 2:
            return Decimal("0" + "." + str(value)[-2:])
        return Decimal(str(value)[:-2] + "." + str(value)[-2:])
    except:
        return Decimal(0)


def moneyout_view(request):
    client = request.user.client
    wallet = client.wallet

    wallet_info = {"amount": int_to_decimal(wallet.amount)}

    success = ""
    errors = ""

    if request.POST:
        if client.wallet and client.wallet.bic and not request.POST.get("bic"):
            bic = client.wallet.bic.replace(" ", "").upper()
        else:
            bic = request.POST.get("bic", "").replace(" ", "").upper()

        if client.wallet and client.wallet.iban and not request.POST.get("iban"):
            iban = client.wallet.iban.replace(" ", "").upper()
        else:
            iban = request.POST.get("iban", "").replace(" ", "").upper()

        try:
            amount = int_to_decimal(int(request.POST.get("amount", "")))
        except Exception:
            amount = None
            errors = "Call us at 0 890 215 315".encode("utf8")
            amount = 0

        if not amount or amount > wallet_info.get("amount"):
            errors = "Amount error".encode("utf8")
            success = ""

        elif bic and iban and amount:
            try:
                wallet.bic = bic
                wallet.iban = iban
                wallet.save()

                now = datetime.now()
                m_o = Moneyout(
                    client=client,
                    bic=bic,
                    iban=iban,
                    amount=amount,
                    date_creation=now,
                    state=0,
                )
                m_o.save()

                response = do_payout(
                    "MONEYOUT-%s" % m_o.pk,
                    amount,
                    DEFAULT_CURRENCY,
                    iban,
                    bic,
                    )

                m_o.response = "{}".format(response)
                m_o.psp_reference = response.get("pspReference", "")

                if response.get("resultCode", "") == "[payout-success]":
                    m_o.state = 1
                    errors = ""
                    success = (
                        "Your payment request has been successfully recorded. "
                        "Go to your wallet page to follow the payment process."
                    )
                else:
                    m_o.state = 6
                    errors = response.get("message", "Please contact Back Market")
                    success = ""

            except Exception as moneyout_error:
                errors = "Ko %s" % moneyout_error

            return HttpResponse(
                json.dumps({"success": success, "errors": errors})
            )