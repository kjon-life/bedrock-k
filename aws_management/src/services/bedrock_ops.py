import boto3
import asyncio

bedrock_client = boto3.client('bedrock')

async def list_available_models() -> list:
    """
    Lists the foundation models currently available in Amazon Bedrock.

    Returns:
        list: A list of dictionaries containing information about available models.
    """
    try:
        response = bedrock_client.list_foundation_models()
        return response['modelSummaries']
    except Exception as e:
        print(f"Error listing models: {str(e)}")
        return []
    
async def invoke_model(prompt: str, model: str = "anthropic.claude-v2") -> str:
    """
    Invokes the specified AI model with the given prompt.

    Args:
        prompt (str): The input prompt for the model.
        model (str): The name of the model to use (default: "anthropic.claude-v2").

    Returns:
        str: The generated response from the model.
    """
    try:
        available_models = await list_available_models()
        model_ids = [m['modelId'] for m in available_models]
        
        if model not in model_ids:
            raise ValueError(f"Model '{model}' is not available. Available models are: {', '.join(model_ids)}")

        # TODO: Implement the actual API call to Bedrock here
        # This is still a placeholder
        response = f"This is a placeholder response for the prompt: {prompt}"
        return response
    except Exception as e:
        print(f"Error invoking model: {str(e)}")
        return ""