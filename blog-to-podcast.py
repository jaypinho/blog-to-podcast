from pathlib import Path
import openai

levine = """
The stylized history of financial exchanges is something like:

1. Once, a dozen or so big brokers met under a tree or whatever to trade their stuff.
2. They collectively set some rules for trading the stuff, which evolved into a nonprofit membership organization — an “exchange” — run by the big brokers.
3. The exchange charged fees to trade, it invested in technology, and it eventually made sense for the exchange to restructure and go public as a for-profit company.
4. The dozen or so big brokers, who once owned and ran the exchange, don’t anymore: It’s a public company, they’ve sold whatever shares they had in it, it’s just an arm’s-length counterparty now.
5. They don’t like paying the fees.
6. They get to talking with each other.
7. “At the end of the day,” they say, “this exchange is really just us. It’s a venue — now a computer system, not a tree, but still — where the 12 of us get together to trade stuff with each other. Why are we paying these fees to a for-profit exchange? Why don’t we just meet together somewhere else, trade with each other, and save on fees?”
8. They can’t literally meet under a different tree, since now everything is computerized, but if they talk about this enough eventually an entrepreneur will go and build it for them.
"""

def text_to_speech(text_str):

    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = openai.audio.speech.create(
        model="tts-1",
        voice="onyx",
        response_format="mp3",
        speed=1.0,
        input=text_str
    )
    response.stream_to_file(speech_file_path)

text_to_speech(levine)