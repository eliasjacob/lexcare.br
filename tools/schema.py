from typing import Literal

from pydantic import BaseModel, Field, field_validator

class Medicamento(BaseModel):
    """
    Representa informações sobre um medicamento mencionado.
    Não inclui suplementos ou fórmulas alimentares/nutricionais.
    """

    nome_comercial: str | None = Field(default=None, description="O nome comercial do medicamento.")
    principio_ativo: str | None = Field(default=None, description="O princípio ativo farmacologicamente ativo do medicamento, sem o nome do sal. NÃO INCLUIR O NOME DO SAL (ex.: citrato de sildenafila -> sildenafila).")
    dosagem: str | None = Field(default=None, description="A dosagem do medicamento, especificando a quantidade e a unidade de medida.")

class Suplemento(BaseModel):
    """
    Representa informações sobre um suplemento ou fórmula alimentar/nutricional mencionado.
    Não inclui medicamentos.
    """

    nome_comercial: str | None = Field(default=None, description="O nome comercial do suplemento ou fórmula alimentar/nutricional.")
    principio_ativo: str | None = Field(default=None, description="O princípio ativo do suplemento ou fórmula alimentar/nutricional.")
    dosagem: str | None = Field(default=None, description="A dosagem do suplemento, especificando a quantidade e a unidade de medida.")

class Doenca(BaseModel):
    """
    Representa informações sobre uma doença mencionada.
    Uma doença pode ter um nome, uma parte do corpo afetada e um código internacional de doenças (CID).
    Todos os campos são opcionais, permitindo que o modelo decline a extração se não houver certeza.
    """

    nome: str | None = Field(default=None, description="O nome da doença, sem incluir a parte do corpo afetada.")
    cid: str | None = Field(default=None, description="O código da Classificação Internacional de Doenças (CID).")

class Procedimento(BaseModel):
    """
    Representa informações sobre um procedimento médico mencionado.
    Um procedimento médico pode ter um nome e um tipo (cirúrgico, diagnóstico ou terapêutico).
    Não inclui medicamentos.
    """

    nome: str = Field(..., description="O nome do procedimento médico")
    tipo: Literal["cirúrgico", "diagnóstico", "terapêutico"] | None  = Field(default=None, description="O tipo do procedimento médico: cirúrgico, diagnóstico ou terapêutico.", enum=["cirúrgico", "diagnóstico", "terapêutico"])
    #tipo: str = Field(..., description="O tipo do procedimento médico: cirúrgico, diagnóstico ou terapêutico.", enum=["cirúrgico", "diagnóstico", "terapêutico"])

class Insumo(BaseModel):
    """
    Representa informações sobre um insumo de saúde mencionado.
    Um insumo médico pode ter um nome e uma quantidade.
    Exemplos de insumos incluem luvas, seringas, máscaras, gazes, fraldas geriátricas, sondas, entre outros.
    Não inclui medicamentos, suplementos ou fórmulas alimentares/nutricionais.
    """

    nome: str = Field(..., description="O nome do insumo médico.")
    quantidade: str | None = Field(default=None, description="A quantidade do insumo médico, especificando a unidade de medida quando aplicável.")

class Pessoa(BaseModel):
    """
    Representa informações sobre uma pessoa mencionada.
    Uma pessoa tem um nome e pode ter um cargo ou função.
    """

    nome: str | None = Field(..., description="O nome completo da pessoa mencionada.")
    funcao_processual: str | None = Field(..., description="A função processual da pessoa mencionada. Pode ser autor, réu, magistrado, médico ou outros.", enum=["autor", "réu", "magistrado", "médico", "outros"])


class ListaMedicamentos(BaseModel):
    """
    Representa uma lista de medicamentos mencionados.
    """

    medicamentos: list[Medicamento] = Field(..., description="Lista de medicamentos mencionados.")

class ListaDoencas(BaseModel):
    """
    Representa uma lista de doenças mencionadas.
    """

    doencas: list[Doenca] = Field(..., description="Lista de doenças mencionadas.")

class ListaSuplementos(BaseModel):
    """
    Representa uma lista de suplementos ou fórmulas alimentares/nutricionais mencionados.
    """

    suplementos: list[Suplemento] = Field(..., description="Lista de suplementos ou fórmulas alimentares/nutricionais mencionados.")

class ListaProcedimentos(BaseModel):
    """
    Representa uma lista de procedimentos médicos mencionados.
    """

    procedimentos: list[Procedimento] = Field(..., description="Lista de procedimentos médicos mencionados.")

class ListaInsumos(BaseModel):
    """
    Representa uma lista de insumos de saúde mencionados.
    """

    insumos: list[Insumo] = Field(..., description="Lista de insumos de saúde mencionados.")

class ListaPessoas(BaseModel):
    """
    Representa uma lista de pessoas mencionadas.
    """

    pessoas: list[Pessoa] = Field(..., description="Lista de pessoas mencionadas.")


class Saude(BaseModel):
    """
    Dados extraídos sobre entidades médicas/saúde. Se nenhum valor for extraído, as listas estarão vazias.
    """

    lista_medicamentos: list[Medicamento] | None = Field(
        default=None, description="Lista de medicamentos mencionados, excluindo suplementos ou fórmulas alimentares/nutricionais."
    )
    lista_doencas: list[Doenca] | None = Field(
        default=None, description="Lista de doenças mencionadas."
    )
    lista_suplementos: list[Suplemento] | None = Field(
        default=None, description="Lista de suplementos ou fórmulas alimentares/nutricionais mencionados, excluindo medicamentos."
    )
    lista_procedimentos: list[Procedimento] | None = Field(
        default=None, description="Lista de procedimentos médicos mencionados."
    )
    lista_insumos: list[Insumo] | None = Field(
        default=None, description="Lista de insumos de saúde mencionados, excluindo medicamentos, suplementos ou fórmulas alimentares/nutricionais."
    )
    lista_pessoas: list[Pessoa] | None = Field(
        default=None, description="Lista de pessoas mencionadas."
    )

    @field_validator("lista_medicamentos", "lista_doencas", "lista_suplementos", "lista_procedimentos", "lista_insumos", "lista_pessoas")
    def convert_none_to_empty_list(cls, value):
        if value is None:
            return []
        return value
    