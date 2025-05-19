# **The Voice Pro**

## **Description**

This project is an interactive Text-to-Speech (TTS) application designed to run within a Google Colab environment. It provides a user-friendly interface to convert text into spoken audio. Key functionalities include support for multiple languages, optional automatic translation of input text to the voice language, adjustable speech speed, and the ability to play or download the generated audio.

## **Features**

* **Multi-Language Support:** Generate speech in various languages using the gTTS library.  
* **Translate to Voice Language:** Automatically translate the input text to the selected voice language before generating speech (leveraging googletrans).  
* **Adjustable Speed:** Control the playback rate of the generated audio.  
* **Generate & Play Audio:** Convert text to speech and play the resulting audio directly within the Google Colab output interface.  
* **Download Audio:** Download the generated speech as an MP3 file.  
* **Interactive UI:** An embedded HTML interface provides a simple way to interact with the application.  
* **Dark Mode:** A toggle is included in the UI to switch to a dark theme.

## **Prerequisites**

* Google Colab environment

## **Installation**

To set up the project in your Google Colab notebook, run the following command in a code cell to install the necessary libraries:

\!pip install gTTS googletrans==4.0.0-rc1

## **Usage**

1. **Open in Google Colab:** Create a new notebook in Google Colab.  
2. **Paste Code:** Copy and paste the entire Python code provided for the application (including the app\_html variable, generate\_speech and download\_speech functions, output.register\_callback calls, and the final display(HTML(app\_html)) line) into a code cell.  
3. **Run Cell:** Execute the code cell.  
4. **Interact:** An interactive HTML interface will appear in the output area of the cell.  
5. **Enter Text:** Type or paste the text you want to convert into the text input area.  
6. **Select Language:** Choose the desired language for the voice from the "Voice Language" dropdown.  
7. **Translate (Optional):** If you want the text to be translated to the chosen voice language, check the "Translate to Voice Language" checkbox.  
8. **Adjust Speed:** Use the "Speed" slider to set the playback speed. The current value is displayed next to the slider.  
9. **Generate Speech:** Click the "Generate" button. A progress bar will show the process, and an audio player will appear below the buttons once the speech is ready.  
10. **Play Audio:** Use the controls on the audio player to listen to the speech.  
11. **Download Audio:** Click the "Download" button to save the audio as an MP3 file (output.mp3) to your local machine.  
12. **Toggle Dark Mode:** Click the switch icon at the top right of the interface to switch between the light and dark themes.

## **How it Works**

The application uses gTTS for the text-to-speech conversion and googletrans for the optional translation feature. The user interface is rendered using HTML, CSS, and JavaScript directly within the Google Colab output. Python functions are exposed to the frontend JavaScript via google.colab.output.register\_callback to handle the speech generation and download requests.

## **Dependencies**

* gTTS  
* googletrans==4.0.0-rc1  
* IPython.display  
* base64

## **Acknowledgments**

* Built with the help of the gTTS and googletrans libraries.  
* Designed to run seamlessly within the Google Colab environment.

## **License**

\[Replace this section with the license information for your project, e.g., MIT, Apache 2.0, etc.\]
