
import urllib
import html
from ts.torch_handler.base_handler import BaseHandler

class MyHandler(BaseHandler):
    """
    Custom handler for pytorch serve. This handler supports batch requests.
    For a deep description of all method check out the doc:
    https://pytorch.org/serve/custom_service.html
    """

    # 获取url并且进行预处理
    def preprocess(self, requests):
        """
        Process all the images from the requests and batch them in a Tensor.
        """
        newQueries = [urllib.parse.unquote(url) for url in requests]
        X_predict = self.vectorizer.transform(newQueries)
        print("--------********----------------------")
        print(X_predict)
        return X_predict,requests

    # 预测结果
    def inference(self,x,requests):
        """
        Given the data from .preprocess, perform inference using the model.
        We return the predicted label for each image.
        """
        preds = self.lgs.predict(x)
        print("--------********----------------------")
        print()
        return preds,requests

    # 返回最终预测结果
    def postprocess(self, preds,requests):
        """
        Given the data from .inference, postprocess the output.
        In our case, we get the human readable label from the mapping 
        file and return a json. Keep in mind that the reply must always
        be an array since we are returning a batch of responses.
        """
        newQueries = [urllib.parse.unquote(url) for url in requests]
        res = []
        for q,r in zip(newQueries, preds):
            tmp = '正常请求' if r == 0 else '恶意请求'
            q_entity = html.escape(q)
            res.append({'url':q_entity, 'res':tmp})
        print("预测的结果列表:{}".format(str(res)))
        return res
