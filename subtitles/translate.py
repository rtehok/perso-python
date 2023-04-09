import argparse
import os
import openai
import time


def translate_text(text, show_name, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Translate the following text from {show_name} to French:\n{text}\n\nFrench:",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()


def translate_subtitle_file(subtitle_file_path, show_name):
    api_key = os.environ.get("OPENAI_API_KEY")
    output_file_path = f"{os.path.basename(subtitle_file_path)}.fr"
    with open(subtitle_file_path, "r") as subtitle_file, open(output_file_path, "w") as output_file:
        lines = subtitle_file.readlines()
        num_lines = len(lines)
        i = 0
        while i < num_lines:
            chunk = "".join(lines[i:i + 20])
            translated_chunk = translate_text(chunk, show_name, api_key)
            output_file.write(translated_chunk + "\n")
            i += 20
            time.sleep(5)  # Add a delay to avoid hitting the OpenAI API rate limit


def main():
    parser = argparse.ArgumentParser(description='Translate subtitle files to French using OpenAI API.')
    parser.add_argument('show_name', type=str, help='the name of the TV show')
    parser.add_argument('subtitle_files', metavar='subtitle_files', type=str, nargs='+',
                        help='a list of subtitle files to translate')
    args = parser.parse_args()

    for subtitle_file_path in args.subtitle_files:
        translate_subtitle_file(subtitle_file_path, args.show_name)


if __name__ == '__main__':
    main()
