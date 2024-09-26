# prediction 결과에서 score, label 하나만 보여주기
def get_max_label(p):
  max_score = 0
  max_label = ""
  for item in p:
      if item['score'] > max_score:
          max_score = item['score']
          max_label = item['label']
  return max_label, max_score

# prediction에서 score만 얻기
def get_score(item):
  return item['score']

# 
def get_max_label2(p):
  max_p = max(p, key=get_score)
  return max_p['label']

# 
def get_max_label3(p):
  max_p = max(p, key=lambda x: x['score'])
  return max_p['label']
