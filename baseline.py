class BaselineClasifier(): # Baseline classifier that predicts the class base on the mode of the labels.
    def __init__(self, np):
        self.central_tendency = None
        self.np = np
        
    def fit(self, data, y, central_t='mode'):
        # Count labels and find the most frequent one 
        label, counts = self.np.unique(y, return_counts=True) 
        if central_t == 'mode':
            self.central_tendency = counts.argmax()
        elif central_t == 'mean':
            self.central_tendency = round(self.np.sum(y)/len(y))
        # Return an array with size equal to the data size  and each element setted to the mode.
        return self
    
    def predict(self, data):
        result = self.np.full(data.shape[0], self.central_tendency)
        return result

def run_clasifier(X_train, y_train, X_test, numpy):
    baseline_clasifier = BaselineClasifier(numpy)
    classifier = baseline_clasifier.fit(X_train, y_train, 'mean')
    return baseline_clasifier.predict(X_test)
