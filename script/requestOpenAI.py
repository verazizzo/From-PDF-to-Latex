from openai import OpenAI
from openAI_key import api_key

def requestoOpenAI(encoded_string, n_page):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
        {
            "role": "system",
            "content": [
            {
                "type": "text",
                "text": f"Write LaTeX code to achieve the following:\nTHIS IS THE IMAGE OF SLIDE {n_page} \n1. Extract the content from the provided image (which is a screenshot of a PDF slide).\n2. Convert the content into LaTeX format, making sure to preserve the following:\n\tHeadings\n\tBullet points\n\tMathematical expressions\n3. Add a comment in the LaTeX file for each slide, indicating the slide’s page number. For example:\n   % Page 1 or % Slide 1\n   This comment should clearly separate the content of each slide.\n4. Write also an associated LaTeX file with explanations for the slides:\n\tMaintain consistency with the formatting.\n\tInclude a page number comment for each explanation (e.g., % Page 1 or % Slide 1).\nDo not include any LaTeX document structure commands, such as \\begin{{document}}, since the content is being inserted into an existing LaTeX file.\nDo not include anything else in the response.\nThe response whould be in this structure:\n\\section{{Content of the slide}}\n%Page {{number of the slide}}\nContent of page 1 goes here.\n\n\n\\section{{Explanation of the slides}}\n%Page {{number of the slide}}\nExplanation of the content of page 1 goes here.\n"
            }
            ]
        },
        {
            "role": "user",
            "content": [
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{encoded_string}",
                },
            }
            ]
        },
        ],
        response_format={
        "type": "text"
        },
        temperature=1,
        max_completion_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response