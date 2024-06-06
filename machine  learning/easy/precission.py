
from sklearn.metrics import precision_score
pred = [1, 1, 0, 1, 0]
actual = [1, 1, 0, 1, 1]

# note  : only for 2 classess case
def recall(actual , pred): 
    tp = 0
    fn = 0
    for idx, _ in enumerate(actual): 
        if pred[idx] == 0: 
            if actual[idx] == 1: 
                fn += 1
        elif pred[idx] == 1: 
            if actual[idx] == 1: 
                tp += 1
    recall_result = tp / (tp + fn)
    return recall_result



def precission(actual , pred): 
    tp = 0
    fn = 0
    for idx, _ in enumerate(actual): 

        if pred[idx] == 1: 
            if actual[idx] == 1: 
                tp += 1
            else: 
                fn += 1
    precision_result = tp / (tp + fn)
    return precision_result
print(f'manually                : {precission(actual=actual, pred= pred)}')
print(f'scikit-learn library    : {precision_score(actual, pred)}')




