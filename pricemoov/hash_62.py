# Designing a URL Shortening service like TinyURL
# Let's design a URL shortening service like TinyURL. This service will provide short aliases redirecting to long URLs.
#
# URL shortening is used to create shorter aliases for long URLs. We call these shortened aliases “short links.” Users are redirected to the original URL when they hit these short links. Short links save a lot of space when displayed, printed, messaged, or tweeted. Additionally, users are less likely to mistype shorter URLs.
#
# For example, if we shorten the following URL through TinyURL:
# https://www.pricemoov.com/aaa/bbb/ccc
#
# We would get:
# https://tinyurl.com/rxcsyr3r
#
# The shortened URL is nearly one-third the size of the actual URL.
#
# URL shortening is used to optimize links across devices, track individual links to analyze audiences, measure ad campaigns’ performance, or hide affiliated original URLs.
# Requirements and Goals of the System
# Functional Requirements:
#
# Must have: Given a URL, our service should generate a shorter and unique alias of it. This is called a short link. This link should be short enough to be easily copied and pasted into applications.
# Must have: When users access a short link, our service should redirect them to the original link.
# Nice to have: Users should optionally be able to pick a custom short link for their URL.
# Nice to have: Links will expire after a standard default timespan. Users should be able to specify the expiration time.
#
# Non-Functional Requirements:
#
# Must have: The system should be highly available. This is required because, if our service is down, all the URL redirections will start failing.
# Must have: URL redirection should happen in real-time with minimal latency.
# Must have: Shortened links should not be guessable (not predictable).
#
# Additional information:
#
# Our system will be read-heavy. There will be lots of redirection requests compared to new URL shortenings. Let’s assume a 100:1 ratio between read and write.
# We will have 500M new URL shortenings per month.

def hash_62(n: int) -> str:
    m = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
         "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
         "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
         "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
         "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    mapping = dict([(i, x) for i, x in enumerate(m)])
    res = []
    while n > 0:
        remainder = n % 62
        res.insert(0, mapping.get(remainder))
        n //= 62

    return "".join(res)


if __name__ == "__main__":
    print(hash_62(2**64-1))
    print(hash_62(2**32-1))
    print(hash_62(2009215674938))
    print(hash_62(11157))
