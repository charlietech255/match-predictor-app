```markdown
# Charlie's Quick AI API

Super simple FastAPI server that talks to OpenAI for you.

Just send a prompt → get answer back.  
Perfect for front-end apps, little tools, prototypes, or when you don't want to show your OpenAI key to the world.

## Features

- FastAPI ⚡
- CORS enabled (works with localhost + deployed frontends)
- Pick model (default: gpt-4o-mini)
- Choose temperature
- One endpoint `/generate`
- Hides your API key safely on the server

## How to use it

```bash
# 1. Clone & go inside
git clone https://github.com/charlietech255/Charlie_ai
cd main

# 2. Install stuff
pip install -r requirements.txt

# 3. Make .env file
echo "OPENAI_API_KEY=sk-..." > .env

# 4. Run!
uvicorn main:app --reload
# or just: python -m uvicorn main:app --reload
```

Server starts → http://localhost:8000

Try it right away:

```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Tell me a very short pirate joke"}'
```

Or open http://localhost:8000/docs → test in Swagger

## Example request (JSON)

```json
{
  "prompt": "Write me a funny 2-sentence bio for a lazy cat",
  "model": "gpt-4o-mini",
  "temperature": 0.9
}
```

Response looks like:

```json
{
  "reply": "Born tired and raised lazy, Whiskers believes naps are an Olympic sport and he's going for gold every afternoon."
}
```

## Made with

- FastAPI
- Pydantic
- python-dotenv
- requests

Made by Charlie 🚀  
(quick & dirty – but it works)

Have fun!
```

Feel free to change the joke or bio example to whatever you like 😄
