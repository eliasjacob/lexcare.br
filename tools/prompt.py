import json
import random
from typing import Any, Dict

from .fewshot import TOOL_USE_EXAMPLES, get_formatted_messages_from_examples
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

FEW_SHOT_NER_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Você é um especialista em extração de entidades nomeadas com precisão excepcional. "
            "Sua tarefa é identificar e extrair informações específicas do texto fornecido, seguindo estas diretrizes:"
            "\n\n1. Extraia as informações exatamente como aparecem no texto, sem interpretações ou alterações."
            "\n2. Se uma informação solicitada não estiver presente ou for ambígua, retorne null para esse campo."
            "\n3. Mantenha-se estritamente dentro do escopo das entidades e atributos definidos no esquema fornecido."
            "\n4. Preste atenção especial para manter a mesma ortografia, pontuação e formatação das informações extraídas."
            "\n5. Não infira ou adicione informações que não estejam explicitamente presentes no texto."
            "\n6. Se houver múltiplas menções da mesma entidade, extraia todas as ocorrências relevantes."
            "\n7. Ignore informações irrelevantes ou fora do contexto das entidades solicitadas."
            "\n\nLembre-se: sua precisão e aderência ao texto original são cruciais para o sucesso desta tarefa."
        ),
        # Placeholder para exemplos de referência, se necessário
        MessagesPlaceholder('examples'),
        ("human", "{text}"),
    ]
)

def generate_few_shot_ner_prompts_json_schema(input_text: str, sample_size: int = 1) -> Dict[str, Any]:
    """Generate few-shot NER prompts using a given example text.

    Args:
        input_text (str): The input text example for generating NER prompts.

    Returns:
        Dict[str, Any]: A dictionary containing the generated NER prompts.
    """
    # Invoke the FEW_SHOT_NER_PROMPT with the provided input text and formatted examples
    sample_examples = random.sample(TOOL_USE_EXAMPLES, sample_size)
    examples = []
    for ex in sample_examples:
        examples.append(HumanMessage(content=ex[0]))
        examples.append(AIMessage(content=json.dumps(ex[1].model_dump(), ensure_ascii=False)))

    ner_prompts = FEW_SHOT_NER_PROMPT.invoke(dict(
        text=input_text,
        examples=examples
    ))
    
    return ner_prompts

def generate_few_shot_ner_prompts(input_text: str) -> Dict[str, Any]:
    """Generate few-shot NER prompts using a given example text.

    Args:
        input_text (str): The input text example for generating NER prompts.

    Returns:
        Dict[str, Any]: A dictionary containing the generated NER prompts.
    """
    # Invoke the FEW_SHOT_NER_PROMPT with the provided input text and formatted examples
    ner_prompts = FEW_SHOT_NER_PROMPT.invoke(dict(
        text=input_text,
        examples=get_formatted_messages_from_examples(TOOL_USE_EXAMPLES)
    ))
    
    return ner_prompts