import gradio as gr
from converter import speech_to_text, text_to_speech
from generator import generate_response

def generate(audio_file):
    if audio_file is None:
        return "", None

    user_input = speech_to_text(audio_file)
    response_text = generate_response(user_input)
    audio_path = text_to_speech(response_text)

    return response_text, audio_path

iface = gr.Interface(
    fn=generate,
    inputs=gr.Audio(sources=["microphone"], type="filepath"),
    outputs=[
        gr.Textbox(label="Response Text"),
        gr.Audio(label="Response Audio", autoplay=True)
    ]
)

# Launch the app
if __name__ == "__main__":
    iface.launch()
