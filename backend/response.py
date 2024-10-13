from groq import Groq

client = Groq()

def main(course="", n_questions="10", n_flashcards="10", topics=[], complexity="medium", type_of_questions="application"):

    message = f"Make {n_questions} {complexity} {type_of_questions} questions on these collective topics: {topics} in a quiz manner with question and then 4 answer choices, followed by a concise explanation. Then, make {n_flashcards} flashcards with a term on one line followed by a memorable description of the term."

    chat_completion = client.chat.completions.create(

        messages=[
            # Set an optional system message. This sets the behavior of the
            # assistant and can be used to provide specific instructions for
            # how it should behave throughout the conversation.
            {
                "role": "system",
                "content": f"you are a {course} teacher who is extraordinary at making quizzes and flashcards that ensure that the student retains the information."
            },
            # Set a user message for the assistant to respond to.
            {
                "role": "user",
                "content": message,
            }
        ],

        model="llama-3.1-70b-versatile",

        # Controls randomness: lowering results in less random completions.
        # As the temperature approaches zero, the model will become deterministic
        # and repetitive.
        temperature=0.5,

        # The maximum number of tokens to generate. Requests can use up to
        # 32,768 tokens shared between prompt and completion.
        max_tokens=8000,

        # Controls diversity via nucleus sampling: 0.5 means half of all
        # likelihood-weighted options are considered.
        top_p=1,

        # A stop sequence is a predefined or user-specified text string that
        # signals an AI to stop generating content, ensuring its responses
        # remain focused and concise. Examples include punctuation marks and
        # markers like "[end]".
        stop=None,

        stream=False,
    )

    return (chat_completion.choices[0].message.content)