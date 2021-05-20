
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ID LPAREN PLUS RPAREN TIMESexpression : expression PLUS termexpression : termterm : term TIMES factorterm : factorfactor : LPAREN expression RPARENfactor : ID'
    
_lr_action_items = {'LPAREN':([0,4,6,7,],[4,4,4,4,]),'ID':([0,4,6,7,],[5,5,5,5,]),'$end':([1,2,3,5,9,10,11,],[0,-2,-4,-6,-1,-3,-5,]),'PLUS':([1,2,3,5,8,9,10,11,],[6,-2,-4,-6,6,-1,-3,-5,]),'RPAREN':([2,3,5,8,9,10,11,],[-2,-4,-6,11,-1,-3,-5,]),'TIMES':([2,3,5,9,10,11,],[7,-4,-6,7,-3,-5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,4,],[1,8,]),'term':([0,4,6,],[2,2,9,]),'factor':([0,4,6,7,],[3,3,3,10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','pyacc.py',6),
  ('expression -> term','expression',1,'p_expression_term','pyacc.py',10),
  ('term -> term TIMES factor','term',3,'p_term_times','pyacc.py',15),
  ('term -> factor','term',1,'p_term_factor','pyacc.py',19),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expression','pyacc.py',24),
  ('factor -> ID','factor',1,'p_factor_ID','pyacc.py',28),
]