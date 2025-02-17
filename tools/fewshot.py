
import uuid
from typing import Dict, List, Tuple, TypedDict

from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
    ToolMessage,
)
from pydantic import BaseModel
from .schema import (
    Doenca,
    Insumo,
    Medicamento,
    Pessoa,
    Procedimento,
    Saude,
    Suplemento,
)

exemplo_1 = """Trata-se de ação proposta por SEVERINO VIEIRA DA SILVA, com pedido de antecipação dos efeitos da tutela, em desfavor da UNIÃO FEDERAL, objetivando a realização de um procedimento cirúrgico (Nefrolitotripsia percutânea + Nefrostomia + Colocação e posterior retirada de cateter duplo J) para o tratamento da doença que lhe acomete (cálculo renal- CID 10 N20), conforme receituário médico (anexo 03), a ser custeado pelo ente federativo demandado.
A parte ré apresentou contestação (anexo 12), por meio da qual arguiu as preliminares de ilegitimidade passiva e de falta de interesse de agir e, no mérito, pugna pela improcedência.
Relatório dispensado, na forma do art. 38 da Lei 9.099/95 c/c o art. 1o da Lei 10.259/01.
I – FUNDAMENTAÇÃO
1. PRELIMINARES
1.1. INTERESSE PROCESSUAL
A viabilidade do exame do mérito da ação depende da coexistência de requisitos denominados condições da ação - cuja ausência deve ser verificada de ofício pelo juiz -, dentre os quais há o interesse processual, configurado no trinômio: necessidade da atividade estatal, utilidade da prestação jurisdicional e adequação do meio utilizado a satisfazer pretensão vindicada.
A função primordial da prestação jurisdicional (solução de lides) deve se limitar a casos em que tal conflito esteja evidenciado, que ascende quando a pretensão de uma parte é resistida pela outra.
No caso em análise, o demandado arguiu a ausência de interesse processual da promovente, tendo em visto que o procedimento pleiteado é fornecido pelo SUS.
Não obstante isso, o fato é que o procedimento não foi fornecido à parte autora, tendo o demandado, inclusive, se manifestado contrariamente aos pedidos formulados nesta demanda, evidenciando, assim, a pretensão resistida e, por consequência, o interesse processual.
Afasto, portanto, a preliminar de ausência de interesse de agir."""

label_1 = Saude(
    lista_medicamentos=[],
    lista_doencas=[
        Doenca(nome="cálculo renal", cid="N20")
    ],
    lista_suplementos=[],
    lista_procedimentos=[
        Procedimento(nome="Nefrolitotripsia percutânea", tipo="cirúrgico"),
        Procedimento(nome="Nefrostomia", tipo="cirúrgico"),
        Procedimento(nome="Colocação e posterior retirada de cateter duplo J", tipo="cirúrgico"),
    ],
    lista_insumos=[],
    lista_pessoas=[Pessoa(nome="SEVERINO VIEIRA DA SILVA", funcao_processual="autor")],
)


exemplo_2 = """Com efeito, a documentação constante dos autos demonstra que o autor, 64 anos de idade, possui histórico familiar de câncer de próstata, tendo apresentado valores elevados em exames de PSA (PSA total 605 ng/ml e PSA livre 20ng/ml) e próstata aumentada de volume (60, 1 cm3, com padrão finamente heterogêneo) que indicam a necessidade de realização urgente do exame requerido, a fim de que possa ser diagnosticado, e, rapidamente, possa ser submetido a tratamento de sua patologia.
Segundo o laudo do oncologista André Aleixo Pereira Hipólito Dantas (CRM/RN 4015), o exame é imprescindível para o diagnóstico, mas, por ser um exame caro, a parte autora não possui condições financeiras para fazê-lo. Nesse ponto, não restam dúvidas a este Juízo da hipossuficiência do grupo familiar do autor, consoante se pode verificar do extrato dos documentos (extrato do CNIS e CTPS) apresentados nos autos.
Destarte, configurado o direito constitucional da parte promovente, impõe-se a procedência deste pedido inicial, seja, o direito à realização do(s) exame(s) pretendido(s).
Ante o exposto, ACOLHO o pedido, resolvendo o mérito, nos termos do art. 487, I, do CPC, para, confirmando a tutela antecipada deferida nos autos, condenar os réus a adotarem as providências cabíveis para que o autor JOSÉ AIRTON DE FREITAS realize o exame médico denominado BIÓPSIA PERCUTANEA ORIENTADA POR TOMOGRAFIA COMPUTADORIZADA / ULTRASSONOGRAFIA/ RESSONANCIA MAGNÉTICA/ RAIO X DA PRÓSTATA, para que possa ser diagnosticado, e, rapidamente, possa ser submetido a tratamento de sua patologia. Adicionalmente, condeno ao fornecimento do fármaco citratrato de sildenafila 50mg, 1 comprimido por dia, pelo prazo de 6 meses, a contar da data da realização do exame, sob pena de multa diária de R$ 500,00 (quinhentos reais), limitada a R$ 10.000,00 (dez mil reais).
Defiro-lhe os benefícios da Assistência Judiciária (Lei 1.060/50)."""


label_2 = Saude(
    lista_medicamentos=[
        Medicamento(
            nome_comercial=None,
            principio_ativo="sildenafila",
            dosagem="50mg",
        ),
    ],
    lista_doencas=[
        Doenca(nome="câncer de próstata", cid=None),
    ],
    lista_suplementos=[],
    lista_procedimentos=[
        Procedimento(
            nome="BIÓPSIA PERCUTANEA ORIENTADA POR TOMOGRAFIA COMPUTADORIZADA",
            tipo="diagnóstico",
        ),
        Procedimento(nome="ULTRASSONOGRAFIA", tipo="diagnóstico"),
        Procedimento(nome="RESSONANCIA MAGNÉTICA", tipo="diagnóstico"),
        Procedimento(nome="RAIO X DA PRÓSTATA", tipo="diagnóstico"),
    ],
    lista_insumos=[],
    lista_pessoas=[
        Pessoa(nome="JOSÉ AIRTON DE FREITAS", funcao_processual="autor"),
        Pessoa(nome="André Aleixo Pereira Hipólito Dantas", funcao_processual="médico"),
    ],
)


exemplo_3 = """Fora deferida a tutela liminar (anexo 20) para que o Estado da Paraíba fornecesse à parte autora os insumos médicos, como 50 (cinquenta) pacotes de gazes, 1 (um) esparadrapo, 1(um) micropore, 1(um) óleo de girassol, 3 (três) frascos de soro, 1 sonda no 18, bem como comprovasse o agendamento para ainda esta semana de acompanhamento nutricional 1 (uma) vez ao mês, de fisioterapia motora e respiratória 2 (duas) vezes por semana.
Expedido alvará para pagamento do tratamento/insumos (anexos 34/35).
Sentença proferida nestes autos (anexo 36) confirmou a tutela, julgando procedente o pleito autoral.
 O Estado da Paraíba não apresentou recurso.
A parte autora, considerando sua situação clínica, requereu a continuidade da prestação dos serviços médicos por um período de 60 dias, apresentando orçamentos (anexos 38 e 39).
A demandante também juntou notas fiscais dos insumos (anexo 40), bem como comprovante de devolução de valores (anexo 41).
Trânsito em julgado se deu em 07/02/2017. (anexo 44)
Instado a cumprir a obrigação, bem como indicar a conta e agência em que foi bloqueado o valor para pagamento da obrigação, com o fim de que se procedesse à devolução do valor constante no anexo 41, o Estado da Paraíba quedou-se inerte.
Passo a decidir."""

label_3 = Saude(
    lista_medicamentos=[],
    lista_doencas=[],
    lista_suplementos=[],
    lista_procedimentos=[
        Procedimento(nome="acompanhamento nutricional", tipo="terapêutico"),
        Procedimento(nome="fisioterapia motora e respiratória", tipo="terapêutico"),
    ],
    lista_insumos=[
        Insumo(nome="gazes", quantidade="50 pacotes"),
        Insumo(nome="esparadrapo", quantidade="1"),
        Insumo(nome="micropore", quantidade="1"),
        Insumo(nome="óleo de girassol", quantidade="1"),
        Insumo(nome="soro", quantidade="3 frascos"),
        Insumo(nome="sonda", quantidade="1"),
    ],
    lista_pessoas=[],
)

exemplo_4 = """NO CASO EM TELA, prospera a pretensão para fornecimento do suplemento nutricional.
Com efeito, as provas anexadas aos autos demonstram que a autora apresenta diagnóstico de Linfoma Não-Hodkin de Alto Grau de Células B (CID10: C.85.1), inclusive submetida ao tratamento quimioterápico, bem como se encontra em estado de desnutrição (22 anos, Peso: 44,7 kg, Altura: 1,60m, IMC: 17,4) em razão de não conseguir suprir as necessidades nutricionais apenas com alimentos, dado o quadro de náuseas que dificulta a aceitação da dieta, sendo necessária a suplementação diária objetivando o aporte adequado de macro e micronutrientes para manutenção do estado nutricional, nos termos do Laudo Médico e avaliação da nutricionista que acompanha a requerente (anexos 08/09).
Cabe destacar, ainda, que a nutricionista responsável pelo atendimento a autora informa que o suplemento industrializado (i) permite a recuperação e manutenção do estado nutricional do paciente devido ao melhor aproveitamento dos nutrientes; (ii) promove o funcionamento intestinal normal; e (iii) possibilita mínima manipulação para o preparo com menores chances de contaminação, o que reduz significativamente riscos de infecções e de morbimortalidade (anexo 09). Acrescenta a nutricionista que “O não uso do suplemente prescrito pode comprometer o estado nutricional do paciente, culminando em complicações que podem levar a novas hospitalizações” (anexo 09).
Comprovada a indispensabilidade do suplemento alimentar prescrito (prioritariamente NUTRIDRINK COMPACT PROTEIN ou, alternativamente, FRESUBIN DRINK PROTEIN POWER ou NUTREN SENIOR – anexo 09, fl. 02) para o tratamento de saúde da autora, resta analisar apenas o requisito da capacidade financeira da família.
Conforme mencionado anteriormente, nos autos do REsp n.o 1657156/RJ, o STJ pacificou o entendimento acerca da necessidade de comprovação da incapacidade financeira do agente de arcar com o custo do tratamento."""

label_4 = Saude(
    lista_medicamentos=[],
    lista_doencas=[
        Doenca(nome="Linfoma Não-Hodkin de Alto Grau de Células B", cid="C.85.1"),
        Doenca(nome="desnutrição", cid=None),
    ],
    lista_suplementos=[
        Suplemento(
            nome_comercial="NUTRIDRINK COMPACT PROTEIN",
            principio_ativo=None,
            dosagem=None,
        ),
        Suplemento(
            nome_comercial="FRESUBIN DRINK PROTEIN POWER",
            principio_ativo=None,
            dosagem=None,
        ),
        Suplemento(nome_comercial="NUTREN SENIOR", principio_ativo=None, dosagem=None),
    ],
    lista_procedimentos=[],
    lista_insumos=[],
    lista_pessoas=[],
)

exemplo_5 = """Nesses termos, presentes os requisitos da verossimilhança das alegações e do perigo da demora, antecipo parcialmente os efeitos da tutela pretendida, ao tempo em que determino que a União Federal, em face da responsabilidade perante o SUS, forneça, de forma gratuita, à Autora, no prazo máximo de cinco dias, os seguintes medicamentos (em relação aos quais não há substituto, nem estão contemplados pela rede pública de saúde): L Carnitina a 10% (um litro e meio por mês), Vitamina B1 (Tiamina) 100mg (30 comprimidos por mês), Vitamina B2 (Riboflavina) 200mg (30 comprimidos por mês) e Vitamina C 500mg (30 comprimidos por mês), Simeticona Gotas (um frasco a cada dois meses), Stimulance (06 caixas por mês) e o Minilax supositório (2 caixas por mês), tudo em quantidade suficiente ao regular tratamento, conforme recomendação médica, sob pena de incidência de multa diária por descumprimento, a ser fixada por este juízo.
No que concerne ao medicamento Depakene - Valproato de Sódio 250 mg/5ml (05 vidros por mês), deve a parte autora adotar os procedimentos necessários à efetivação de seu cadastro junto à Secretaria Municipal de Saúde para recebimento nas farmácias pólo da Secretaria Executiva Regional (SER), haja vista que o mesmo é fornecido pela rede pública.
Intime-se, imediatamente, a ré para cumprir esta ordem.
Cite-se no prazo legal a União, na pessoa do Chefe da Advocacia da União no Ceará."""


label_5 = Saude(
    lista_medicamentos=[
        Medicamento(
            nome_comercial="Simeticona",
            principio_ativo=None,
            dosagem=None,
        ),
        Medicamento(
            nome_comercial="Stimulance",
            principio_ativo=None,
            dosagem=None,
        ),
        Medicamento(
            nome_comercial="Minilax",
            principio_ativo=None,
            dosagem=None,
        ),
        Medicamento(
            nome_comercial="Depakene",
            principio_ativo="Valproato",
            dosagem="250 mg/5ml",
        ),
    ],
    lista_doencas=[],
    lista_suplementos=[
        Suplemento(
            nome_comercial=None,
            principio_ativo="L Carnitina",
            dosagem="10%",
        ),
        Suplemento(
            nome_comercial="Vitamina B1",
            principio_ativo="Tiamina",
            dosagem="100mg",
        ),
        Suplemento(
            nome_comercial="Vitamina B2",
            principio_ativo="Riboflavina",
            dosagem="200mg",
        ),
        Suplemento(
            nome_comercial="Vitamina C",
            principio_ativo=None,
            dosagem="500mg",
        ),

    ],
    lista_procedimentos=[],
    lista_insumos=[],
    lista_pessoas=[],
)

exemplo_6 = """a) no prazo de quinze (15) dias, forneça 24 caixas de CEBRALAT (Cilostazol); 13 caixas de PANTOBRAZOL; 24 caixas de ATENOLOL; 12 caixas de VASTAREL (Dicloridrato de Trimatazidina); 12 caixas de JARDIANCE (Empaglifozina); 12 caixas de NESINA + NET (Benzoato de Alogiptina e Cloridrato de Metformina); 12 caixas de STANGLIT (Cloridrato de Pioglitazona); e 12 caixas de FRESH TEARS, garantindo o tratamento por um período de doze (12) meses, sob pena de multa fixa de R$ 300,00. Excepcionalmente, em razão da urgência na continuidade do tratamento, a UNIÃO poderá, alternativamente, cumprir o julgado, realizando o depósito judicial no valor de R$ 7.221,95, no mesmo prazo acima e sob as mesmas penas.
Em caso de descumprimento, será expedida uma RPV no valor de R$ 300,00, além da expedição de RPV no valor do tratamento anual (R$ 7.221,95), a ser revertida em favor da parte autora. Oficie-se ainda ao TCU para apurar responsabilidade pelo dano relativo à multa aplicada, e arquive-se.
Se a União comprovar o depósito nos próximos 30 dias, a multa ficará mantida e será cancelada a RPV para o custeio do tratamento. Como os autos estarão no arquivo, caberá à União, após peticionar comprovando o depósito, comunicar à Secretaria da Vara por e-mail para desarquivamento dos autos, cancelamento da RPV e liberação do depósito ao autor.
a. cumprida a diligência e efetuado o depósito judicial pela parte ré, intime-se ao(à) Gerente da instituição financeira em que o valor foi depositado a fim de que se proceda a transferência do montante para conta de titularidade da empresa fornecedora de medicamentos;
b. A parte autora fica obrigada a comprovar a aquisição dos fármacos, mediante nota fiscal, no prazo de 05 (cinco) dias, a contar da transferência supramencionada, sob pena de promover a devolução dos valores recebidos."""


label_6 = Saude(
    lista_medicamentos=[
        Medicamento(
            nome_comercial="CEBRALAT", principio_ativo="Cilostazol", dosagem=None
        ),
        Medicamento(nome_comercial=None, principio_ativo="PANTOBRAZOL", dosagem=None),
        Medicamento(nome_comercial=None, principio_ativo="ATENOLOL", dosagem=None),
        Medicamento(
            nome_comercial="VASTAREL", principio_ativo="Trimatazidina", dosagem=None
        ),
        Medicamento(
            nome_comercial="JARDIANCE", principio_ativo="Empaglifozina", dosagem=None
        ),
        Medicamento(
            nome_comercial="NESINA + NET",
            principio_ativo="Alogiptina",
            dosagem=None,
        ),
        Medicamento(
            nome_comercial="NESINA + NET",
            principio_ativo="Metformina",
            dosagem=None,
        ),
        Medicamento(
            nome_comercial="STANGLIT",
            principio_ativo="Pioglitazona",
            dosagem=None,
        ),
        Medicamento(nome_comercial="FRESH TEARS", principio_ativo=None, dosagem=None),
    ],
    lista_doencas=[],
    lista_suplementos=[],
    lista_procedimentos=[],
    lista_insumos=[],
    lista_pessoas=[],
)


exemplo_7 = """'De acordo com a Suprema Corte, deve-se, primeiramente, aferir a existência de alguma política pública que ampare a prestação pleiteada. Assim, em se encontrando a prestação de saúde pretendida incluída dentre as políticas públicas formuladas pelo SUS, a pretensão deduzida afigurar-se-á como um direito subjetivo público do particular a reclamar do Estado o seu devido cumprimento.\nPor outro lado, não estando a prestação de saúde pretendida amparada pelas políticas estatais existentes, tendo em vista que o SUS se filiou à corrente da “Medicina com base em evidências”, a adoção de um medicamento ou tratamento que não se encontre em conformidade com os protocolos clínicos estabelecidos deve ser vista com reservas, porquanto tende a contrariar o consenso científico então vigente. Deve-se, pois, privilegiar, em princípio, o tratamento fornecido pelo SUS, de modo que a concessão de medidas liminares em matérias relativas às tutelas de saúde reclama redobrada cautela, não prescindindo da inequívoca comprovação da ineficácia ou impropriedade da política de saúde existente.\nRessalte-se, nesse ponto, que a existência de política estatal que abranja a prestação de saúde ora pleiteada pela parte autora, ab initio, é a condição necessária à apreciação da liminar.\nNa hipótese vertente, a verossimilhança das alegações da parte autora, bem como o periculum in mora, restaram evidentes, podendo-se facilmente extraí-los dos exames médicos, declaração e da negativa do NIJUS (docs. 05/09).\nOutrossim, o alto custo do medicamento, agravado, no caso, por ser a parte autora desprovida de condições financeiras para custeá-los, implica em uma necessidade de provimento jurisdicional.\nDestarte, restando efetivamente demonstrado o direito público subjetivo da parte autora, fundado na imprescindibilidade de ser ingerido o medicamento prescrito ao tratamento do autor, não comportando, portanto, maiores controvérsias acerca da questão, sou pelo deferimento, em parte, da liminar requestada.'"""

label_7 = Saude(
    lista_medicamentos=[],
    lista_doencas=[],
    lista_suplementos=[],
    lista_procedimentos=[],
    lista_insumos=[],
    lista_pessoas=[],
)

exemplo_8 =     """DECISÃO
Vistos etc.
Trata-se de ação de obrigação de fazer com pedido de tutela de urgência ajuizada por Maria da Silva em face do Estado de São Paulo, objetivando o fornecimento do medicamento SPINRAZA (Nusinersena) 12mg/5ml, para tratamento de Atrofia Muscular Espinhal (AME) Tipo II.
A autora, menor impúbere de 4 anos de idade, representada por seus genitores, alega ser portadora de AME Tipo II, doença neurodegenerativa rara e grave, conforme laudo médico e exames genéticos anexados aos autos. Afirma que o medicamento pleiteado é o único tratamento eficaz disponível para sua condição, tendo sido aprovado pela ANVISA, mas ainda não incorporado ao SUS devido ao alto custo."""

label_8 = Saude(
    lista_medicamentos=[
        Medicamento(
            nome_comercial="SPINRAZA",
            principio_ativo="Nusinersena",
            dosagem="12mg/5ml",
        ),
    ],
    lista_doencas=[
        Doenca(nome="Atrofia Muscular Espinhal", cid=None),
        Doenca(nome="AME", cid=None),
    ],
    lista_suplementos=[],
    lista_procedimentos=[],
    lista_insumos=[],
    lista_pessoas=[Pessoa(nome="Maria da Silva", funcao_processual="autor")],
)


exemplo_9 = """. Autos no 0000000-11.2222.3.44.5555, rel. Francisco Glauber Pessoa Alves, composição, ainda, dos Juízes Federais Juiz Almiro José da Rocha Lemos (2a Relatoria) e Carlos Wagner Dias Ferreira (Presidência e 1a Relatoria), data de julgamento 16.05.2018. 14. Conforme Nota Técnica CONJUR (anexo 21), o SUS oferece para o tratamento do déficit de atenção e hiperatividade os seguintes medicamentos: carbonato de lítio, valproato de sódio ou ácido valpróico. Ocorre que, consoante se observa do laudo médico que acompanha a inicial (anexo 06), o autor somente fez uso de cloridrato metilfenidato de ação rápida e dimesilato de lisdexanfetamina. Não houve utilização ou tentativa de utilização das demais alternativas existentes no SUS. 15. Claro que as demandas envolvendo prescrição de medicamento são tratadas caso-a-caso, na medida em que não apenas a resposta de cada paciente é diferente, mas, sobretudo, o histórico de cada situação é diverso. Como já dito, sem grave ofensa ao princípio republicano não se pode desconsiderar a alternativa existente no âmbito do SUS, presumindo ser ela ineficaz, devendo restar comprovada concretamente a ineficácia na sua situação específica, o que, infelizmente, no caso examinado não ocorreu, já que não houve esgotamento das alternativas ofertadas pelo Sistema Único de Saúde. 16'"""

label_9 = Saude(
    lista_medicamentos=[
        Medicamento(
            nome_comercial=None,
            principio_ativo="lítio",
            dosagem=None,
        ),
        Medicamento(
            nome_comercial=None,
            principio_ativo="valproato",
            dosagem=None,
        ),
        Medicamento(
            nome_comercial=None,
            principio_ativo="ácido valpróico",
            dosagem=None,
        ),
        Medicamento(
            nome_comercial=None,
            principio_ativo="metilfenidato",
            dosagem=None,
        ),
        Medicamento(
            nome_comercial=None,
            principio_ativo="lisdexanfetamina",
            dosagem=None,
        ),
    ],
    lista_doencas=[
        Doenca(nome="déficit de atenção e hiperatividade", cid=None)
    ],
    lista_suplementos=[],
    lista_procedimentos=[],
    lista_insumos=[],
    lista_pessoas=[
        Pessoa(nome="Francisco Glauber Pessoa Alves", funcao_processual="magistrado"),
        Pessoa(nome="Almiro José da Rocha Lemos", funcao_processual="magistrado"),
        Pessoa(nome="Carlos Wagner Dias Ferreira", funcao_processual="magistrado"),
    ],
)


TOOL_USE_EXAMPLES = [
    (exemplo_1, label_1),
    (exemplo_2, label_2),
    (exemplo_3, label_3),
    (exemplo_4, label_4),
    (exemplo_5, label_5),
    (exemplo_6, label_6),
    (exemplo_7, label_7),
    (exemplo_8, label_8),
    (exemplo_9, label_9),
]
#%%


class Example(TypedDict):
    """A representation of an example consisting of text input and expected tool calls.

    For extraction, the tool calls are represented as instances of pydantic model.
    """

    input: str  # This is the example text
    tool_calls: List[BaseModel]  # Instances of pydantic model that should be extracted


def convert_tool_example_to_messages(example: Example) -> List[BaseMessage]:
    """Convert an example into a list of messages that can be fed into an LLM.

    This code is an adapter that converts our example to a list of messages
    that can be fed into a chat model.

    The list of messages per example corresponds to:

    1) HumanMessage: contains the content from which content should be extracted.
    2) AIMessage: contains the extracted information from the model
    3) ToolMessage: contains confirmation to the model that the model requested a tool correctly.

    The ToolMessage is required because some of the chat models are hyper-optimized for agents
    rather than for an extraction use case.
    """
    messages: List[BaseMessage] = [HumanMessage(content=example["input"])]
    tool_calls = []
    for tool_call in example["tool_calls"]:
        tool_calls.append(
            {
                "id": str(uuid.uuid4()),
                "args": tool_call.model_dump(),
                # The name of the function right now corresponds
                # to the name of the pydantic model
                # This is implicit in the API right now,
                # and will be improved over time.
                "name": tool_call.__class__.__name__,
            },
        )
    messages.append(AIMessage(content="", tool_calls=tool_calls))
    tool_outputs = example.get("tool_outputs") or [
        "You have correctly called this tool."
    ] * len(tool_calls)
    for output, tool_call in zip(tool_outputs, tool_calls):
        messages.append(ToolMessage(content=output, tool_call_id=tool_call["id"]))

    return messages


def get_formatted_messages_from_examples(examples: List[Tuple[str, str]]) -> List[Dict[str, BaseMessage]]:
    """Generate a list of formatted messages from a list of examples.

    Args:
        examples (list[tuple[str, str]]): A list of tuples where each tuple contains
                                          a text input and a corresponding tool call.

    Returns:
        list[BaseMessage]: A list of formatted messages.
    """
    formatted_messages = []

    for text_input, tool_call in examples:
        # Convert each example to a list of messages and extend the formatted_messages list
        formatted_messages.extend(
            convert_tool_example_to_messages({"input": text_input, "tool_calls": [tool_call]})
        )
    
    return formatted_messages
