

# Hello! Should we prompt?

I've been a builder 🍀 all my life. 

The arc of 'AI' allows us to build information within context to create value. As product, that means we build something which solves an experience problem, or a business problem, or both, and someone is willing to pay for our solution. 

Let me be succinct:  If no one is paying me for this (yet), and since it produces delight in me, perhaps it is art?

The project has four de rigueur systems:

1. A code generation model.
2. A chat history summarization model.
3. Retrieval augmented generation (RAG) model.
4. A Diffusion generator.

<img align="right" width="300" src="https://user-images.githubusercontent.com/76539355/214731371-78cb7bcb-996d-4108-9872-7af758ed5647.png" alt="A Maia">



# kjon &middot; prompt  
[![Fly Deploy](https://github.com/kjon-life/bedrock-k/actions/workflows/fly.yml/badge.svg)](https://github.com/kjon-life/bedrock-k/actions/workflows/fly.yml) 
 ![GitHub commit activity](https://img.shields.io/github/commit-activity/y/kjon-life/bedrock-k) 
 ![GitHub License](https://img.shields.io/github/license/kjon-life/bedrock-k)
 ![GitHub top language](https://img.shields.io/github/languages/top/kjon-life/bedrock-k)
 ![W3C Validation](https://img.shields.io/w3c-validation/html?targetUrl=https%3A%2F%2Fkjon.life) 
 
This is a project that feeds my developer portfoio. To connect:  
- Mention me in an issue or pull request: @kjon-life  
- My friends connect on [Instagram: @kilo.jon](https://www.instagram.com/kilo.jon/)   
- [LinkedIn](https://www.linkedin.com/in/jonhwilliams) for professional connections.

### About:  
- I work in the intersections of infrastructure, performance, and revenue.  
- I am deeply curious about LLM systems which assist people to solve with accuracy, speed, utility, and delight. 
- I am working on enterprise LLMs with traceability to the original factual source. 
- We augment open source LLMs for domain-specific and proprietary data in contextual relevance. 
- We write software which we ourselves, use... 

### Project Overview:
* App code is a simple Go web server 
* The app is containerized into a Docker image called `bedrock-k` 
* The Dockerfile uses a Go builder image to compile the app code and copies the binary into a minimal final image
* The app can be manually deployed using flyctl from the fly.toml config file
* GitHub Actions deploys main to dev automatically

### Tech stack:
* Python - for well, everything
* Bedrock - for accessing a wide range of models
* Pinecone - for storing and querying the RAG data
* LangChain - for building applications with LLMs  
* pre-commit - for code quality and keeping the infrastructure DRY
* Poetry - for dependency management
    * [Poetry](https://python-poetry.org/) is a tool for dependency management in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.
    * [ruff](https://beta.ruff.rs/docs/configuration/) ensure that code adheres to PEP 8 standards.
* Parcel - for preprocessing SCSS and JS bundling
* Go - for the app code
* Docker - for unit of deployment
* flyctl - for manual deployment
* GitHub Actions - for CI/CD
* Fly.io - for the serverless hosting platform

```flyctl``` is a CLI tool from [Fly.io](http://fly.io)
You can read about it [here](https://fly.io/docs/hands-on/).

### History:  

### Roadmap: Build and Scale Generative AI on AWS
[Q3](not available) WIP
   

### Acknowledgements:

This project [depends](https://github.com/kjon-life/bedrock-k/network/dependencies) on the copious contributions of others including:

- [Cursor](https://www.cursor.com/) because it works in conditions that seem designed to make someone quit. 
- [Perplexity](https://www.perplexity.ai/) 
    - and the [pplx-api](https://docs.perplexity.ai/docs/getting-started) 
- [Amazon Q](https://github.com/aws/aws-toolkit-vscode) in ~~VS Code~~ Cursor
- [Cursor](https://www.cursor.com/) on Darwin

This project is possible because of these and other services:

- [Porkbun](https://porkbun.com/) - Domain registration and DNS management
- [Fly.io](https://fly.io/) - Application hosting platform

This project is possible because of these and other people:


- [ZTM](https://zerotomastery.io/courses/) - for 342+ days of work done in  Python, Rust, Django, SCSS, prompt engineering, full stack, automation, AWS certification, business analytics, statistics, AWS Bedrock, OpenAI API, LangChain, Streamlit, Pinecone,... 