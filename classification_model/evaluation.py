import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, recall_score, precision_score, \
     accuracy_score, roc_auc_score, f1_score, matthews_corrcoef


def generate_report(y_true: list, y_pred: list):
    report = pd.DataFrame(classification_report(y_true=y_true, y_pred=y_pred, output_dict=True)).T
    return report


def confusion_matrix(y_true: list, y_pred: list, normalize: bool = True):
    if normalize:
        table = np.round(pd.crosstab(index=y_true, columns=y_pred,
                                     rownames=['Observado'], colnames=['Predicho'], normalize='index'), 2)
    else:
        table = np.round(pd.crosstab(index=y_true, columns=y_pred, rownames=['Observed'], colnames=['Predicted']), 2)
    table = table.rename(columns={0.: 'Activo', 1.: 'Desercion'},
                         index={0.: 'Activo', 1.: 'Desercion'})
    return table


def metrics_summary(y_true: list, y_pred: list):
    metrics = {
        'roc': roc_auc_score(y_true=y_true, y_score=y_pred),
        'accuracy': accuracy_score(y_true=y_true, y_pred=y_pred),
        'precision': precision_score(y_true=y_true, y_pred=y_pred),
        'recall': recall_score(y_true=y_true, y_pred=y_pred),
        'f1': f1_score(y_true=y_true, y_pred=y_pred),
        'matthews_coef': matthews_corrcoef(y_true=y_true, y_pred=y_pred)
    }
    print(f'El área bajo la curva ROC es: {metrics["roc"]}')
    print(f'La exactitud es: {metrics["accuracy"]}')
    print(f'La precisión es: {metrics["precision"]}')
    print(f'El recall es: {metrics["recall"]}')
    print(f'El puntaje F1 es: {metrics["f1"]}')
    print(f'El coeficiente de correlación de Matthews es: {metrics["matthews_coef"]} \n')
