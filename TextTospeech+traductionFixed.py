!pip install gTTS googletrans==4.0.0-rc1
from gtts import gTTS
from googletrans import Translator
from IPython.display import Audio, display, HTML
import base64


app_html = """
<div class="tts-app" id="tts-app">
  <style>
    :root {
      --primary: #6366f1;
      --primary-dark: #4f46e5;
      --text: #1e293b;
      --bg: #f8fafc;
      --card: #ffffff;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }

    .dark-mode {
      --primary: #818cf8;
      --primary-dark: #6366f1;
      --text: #f1f5f9;
      --bg: #0f172a;
      --card: #1e293b;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
    }

    .tts-app {
      font-family: 'Segoe UI', system-ui, sans-serif;
      max-width: 650px;
      margin: 0 auto;
      padding: 2rem;
      color: var(--text);
      background: var(--bg);
      min-height: 100vh;
      transition: all 0.3s ease;
    }

    .tts-card {
      background: var(--card);
      border-radius: 1rem;
      padding: 2rem;
      box-shadow: var(--shadow);
      transition: all 0.3s ease;
    }

    .tts-title {
      font-size: 2rem;
      font-weight: 700;
      margin-bottom: 1.5rem;
      background: linear-gradient(90deg, var(--primary), #ec4899);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
      text-align: center;
    }

    .form-group {
      margin-bottom: 1.75rem;
    }

    .form-group label {
      display: block;
      margin-bottom: 0.6rem;
      font-weight: 600;
      color: var(--text);
    }

    .tts-input {
      width: 100%;
      min-height: 150px;
      padding: 1rem;
      border: 1px solid #e2e8f0;
      border-radius: 0.5rem;
      font-size: 1rem;
      transition: all 0.3s;
      resize: vertical;
    }

    .tts-input:focus {
      outline: none;
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
    }

    .tts-select {
      width: 100%;
      padding: 0.8rem;
      border: 1px solid #e2e8f0;
      border-radius: 0.5rem;
      font-size: 1rem;
      transition: all 0.3s;
    }

    .tts-select:focus {
      outline: none;
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
    }

    .tts-slider-container {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .tts-slider {
      flex-grow: 1;
    }

    .tts-slider-value {
      width: 40px;
      text-align: right;
      color: var(--text);
      font-weight: 500;
    }

    .progress-bar {
      height: 8px;
      background: #e2e8f0;
      border-radius: 4px;
      margin-bottom: 1.75rem;
      overflow: hidden;
    }

    .progress-fill {
      height: 100%;
      background: linear-gradient(90deg, var(--primary), #ec4899);
      width: 0%;
      border-radius: 4px;
      transition: width 0.3s ease;
    }

    .status-message {
      padding: 1rem;
      border-radius: 0.5rem;
      margin-bottom: 1.75rem;
      display: none;
      font-weight: 500;
    }

    .success {
      background: #dcfce7;
      color: #166534;
      border: 1px solid #bbf7d0;
    }

    .error {
      background: #fee2e2;
      color: #991b1b;
      border: 1px solid #fca5a5;
    }

    .dark-mode .success {
      background: #166534;
      color: #dcfce7;
      border-color: #4ade80;
    }

    .dark-mode .error {
      background: #991b1b;
      color: #fee2e2;
      border-color: #f87171;
    }

    .action-buttons {
      display: flex;
      gap: 1rem;
      justify-content: flex-end;
    }

    .icon-button {
      background: var(--primary);
      color: white;
      border: none;
      padding: 0.8rem 1.5rem;
      border-radius: 0.5rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
    }

    .icon-button:hover {
      background: var(--primary-dark);
      transform: translateY(-1px);
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .icon-button:active {
      transform: translateY(0);
    }

    .dark-mode .icon-button {
      background: var(--primary);
      color: var(--text);
    }

    .dark-mode .icon-button:hover {
      background: var(--primary-dark);
      color: white;
    }

    .toggle-container {
      display: flex;
      justify-content: flex-end;
      margin-bottom: 1.5rem;
    }

    .toggle-switch {
      position: relative;
      display: inline-block;
      width: 60px;
      height: 30px;
    }

    .toggle-switch input {
      opacity: 0;
      width: 0;
      height: 0;
    }

    .toggle-slider {
      position: absolute;
      cursor: pointer;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background-color: #ccc;
      transition: .4s;
      border-radius: 34px;
    }

    .toggle-slider:before {
      position: absolute;
      content: "";
      height: 22px;
      width: 22px;
      left: 4px;
      bottom: 4px;
      background-color: white;
      transition: .4s;
      border-radius: 50%;
    }

    input:checked + .toggle-slider {
      background-color: var(--primary);
    }

    input:checked + .toggle-slider:before {
      transform: translateX(30px);
    }

    .checkbox-container {
      display: flex;
      align-items: center;
      margin-bottom: 1rem;
    }

    .checkbox-container label {
      margin-left: 0.5rem;
      font-weight: normal;
    }
  </style>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <div class="toggle-container">
    <label class="toggle-switch">
      <input type="checkbox" id="dark-mode-toggle">
      <span class="toggle-slider"></span>
    </label>
  </div>
  <div class="tts-card">
    <h1 class="tts-title">🎤 The Maram Voice Pro</h1>
    <div class="form-group">
      <label for="text-input">Enter Text:</label>
      <textarea class="tts-input" id="text-input" placeholder="Type or paste your text here..."></textarea>
    </div>
    <div class="checkbox-container">
      <input type="checkbox" id="translate-checkbox">
      <label for="translate-checkbox">Translate to Voice Language</label>
    </div>
    <div class="progress-bar">
      <div class="progress-fill" id="progress-bar"></div>
    </div>
    <div class="status-message" id="status-message"></div>
    <div class="form-group">
      <label for="language-select">Voice Language:</label>
      <select id="language-select" class="tts-select">
        <option value="en">English</option>
        <option value="es">Spanish</option>
        <option value="fr">French</option>
        <option value="de">German</option>
        <option value="it">Italian</option>
        <option value="pt">Portuguese</option>
        <option value="ru">Russian</option>
        <option value="ja">Japanese</option>
        <option value="zh-CN">Chinese</option>
        <option value="ar">Arabic</option>
      </select>
    </div>
    <div class="form-group">
      <label for="speed-slider">Speed:</label>
      <div class="tts-slider-container">
        <input type="range" min="0.5" max="2" step="0.1" value="1" class="tts-slider" id="speed-slider">
        <span class="tts-slider-value" id="speed-value">1.0x</span>
      </div>
    </div>
    <div class="action-buttons">
      <button class="icon-button" id="play-button" title="Generate Speech">
        <i class="fas fa-play"></i> Generate
      </button>
      <button class="icon-button" id="download-button" title="Download MP3">
        <i class="fas fa-download"></i> Download
      </button>
    </div>
    <div id="audio-container"></div>
  </div>
</div>
<script>

document.getElementById('dark-mode-toggle').addEventListener('change', function() {
  document.getElementById('tts-app').classList.toggle('dark-mode');
});


const speedSlider = document.getElementById('speed-slider');
const speedValue = document.getElementById('speed-value');
speedSlider.addEventListener('input', function() {
  speedValue.textContent = parseFloat(this.value).toFixed(1) + 'x';
});


function showStatus(message, type) {
  const status = document.getElementById('status-message');
  status.textContent = message;
  status.className = 'status-message ' + type;
  status.style.display = 'block';
  setTimeout(() => {
    status.style.opacity = '0';
    setTimeout(() => {
      status.style.display = 'none';
      status.style.opacity = '1';
    }, 300);
  }, 3000);
}


document.getElementById('play-button').addEventListener('click', function() {
  const text = document.getElementById('text-input').value;
  const lang = document.getElementById('language-select').value;
  const speed = parseFloat(document.getElementById('speed-slider').value);
  const translate = document.getElementById('translate-checkbox').checked;
  if (!text.trim()) {
    showStatus("Please enter some text first!", "error");
    return;
  }

  const progressBar = document.getElementById('progress-bar');
  progressBar.style.width = '0%';
  let progress = 0;
  const interval = setInterval(() => {
    progress += 5;
    progressBar.style.width = progress + '%';
    if (progress >= 100) clearInterval(interval);
  }, 50);
 
  google.colab.kernel.invokeFunction('generate_speech', [text, lang, speed, translate], {});
});


document.getElementById('download-button').addEventListener('click', function() {
  google.colab.kernel.invokeFunction('download_speech', [], {});
});
</script>
"""


def generate_speech(text, lang='en', speed=1.0, translate=False):
  try:
    if translate:
      translator = Translator()
      translation = translator.translate(text, dest=lang)
      text_to_speak = translation.text
    else:
      text_to_speak = text
    tts = gTTS(text=text_to_speak, lang=lang, slow=False)
    tts.save("output.mp3")
    
    audio_html = f"""
    <audio controls autoplay style="width:100%; margin-top:1rem;">
      <source src="data:audio/mp3;base64,{base64.b64encode(open('output.mp3','rb').read()).decode()}" type="audio/mp3">
      <script>
        document.querySelector('audio').playbackRate = {speed};
      </script>
    </audio>
    """
    display(HTML(f'<div id="audio-player">{audio_html}</div>'), display_id='audio-container')
  
    display(HTML("""
    <script>
    showStatus("Speech generated successfully!", "success");
    </script>
    """))
  except Exception as e:
    display(HTML(f"""
    <script>
    showStatus("Error: {str(e)}", "error");
    </script>
    """))

def download_speech():
  try:
    from google.colab import files
    files.download("output.mp3")
    display(HTML("""
    <script>
    showStatus("Download started!", "success");
    </script>
    """))
  except ImportError:
    display(HTML("""
    <script>
    showStatus("Download only works in Google Colab", "error");
    </script>
    """))
  except Exception as e:
    display(HTML(f"""
    <script>
    showStatus("Error during download: {str(e)}", "error");
    </script>
    """))

from google.colab import output
output.register_callback('generate_speech', generate_speech)
output.register_callback('download_speech', download_speech)
display(HTML(app_html))