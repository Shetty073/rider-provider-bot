from chatterbot import ChatBot, comparisons, response_selection
from chatterbot.trainers import ChatterBotCorpusTrainer

cb = ChatBot(
    "Simba",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": comparisons.LevenshteinDistance,
            "response_selection_method": response_selection.get_first_response
        }
    ]
)

trainer = ChatterBotCorpusTrainer(cb)



