# Shared building blocks for the auto-checked exercise files (items_mNN.py).
# Same format as Module 1 (app_items.py): every control has exactly one correct answer, given as the option text.
#   M(id, prompt, options, answer, sol=None)            single choice
#   G(id, prompt, columns, rows, sol=None)              table: rows are (label, [cell, …]); a cell is (options, answer) or None
# `sol` names the worked solution to show (an answers-file key such as '3I-2' or 'B2'); by default the item's own id.
# Use SOLMD('…markdown…') as `sol` when the answers file has no worked solution for the item.
from app_items import M, G, CLS, CASE, SIGN, END, ENDA


def R(bank, pairs):
    """Rows for a one-column table whose cells all share one option bank."""
    return [(label, [(bank, ans)]) for label, ans in pairs]


def SOLMD(md):
    return 'md:' + md


TF = ['True', 'False']
YN = ['Yes', 'No']
