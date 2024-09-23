# prompt2pic

## Overview

prompt2pic is a powerful image generation tool that leverages OpenAI's DALL-E model to transform text prompts into stunning visuals. This project provides a simple, yet flexible interface for AI-powered image creation, making it easy for developers, creators, and AI enthusiasts to bring their ideas to life.

## Features

- Text-to-image generation using OpenAI's DALL-E model
- Support for negative prompts to refine image output
- Customizable image sizes (1024x1024, 1792x1024, or 1024x1792 for DALL-E 3)
- Easy integration with existing projects
- Simple Python API for image generation

## Use Cases

prompt2pic is ideal for a variety of applications, including:

- Creation of custom imagery for websites, emails, and digital content
- Generation of concept art for various media forms
- Rapid prototyping of visual ideas
- Educational tools for exploring AI and machine learning
- Personal creative projects and artistic experimentation

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/bdeva1975/prompt2pic.git
   cd prompt2pic
   ```

2. Install required packages:
   ```
   pip install openai python-dotenv requests
   ```

3. Set up your OpenAI API key in a `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Here's a basic example of how to use prompt2pic:

```python
from prompt2pic import get_image_from_model

prompt = "A serene lake surrounded by mountains at sunset"
negative_prompt = "No people, no buildings"

image_bytes = get_image_from_model(prompt, negative_prompt)

if image_bytes:
    with open("generated_image.png", "wb") as f:
        f.write(image_bytes.getvalue())
    print("Image generated and saved as 'generated_image.png'")
else:
    print("Failed to generate image")
```

## Contributing

Contributions to prompt2pic are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for providing the DALL-E API
- All contributors and users of this project
