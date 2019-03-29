# import argparse
# import logging
# import re
# from sklearn.externals import joblib
from core import test


# def parse_args():
#     """
#     Parse command line arguments
#     """
#     parser = argparse.ArgumentParser(description='Sentiment Analysis')
#     parser.add_argument('--model', nargs='+', default=['svm'], help='svm, bayes or dict')
#     parser.add_argument('--log_path', help='path of the log file. If not set, logs are printed to console')
#
#     return parser.parse_args()
#
#
# def run():
#     args = parse_args()
#
#     logger = logging.getLogger('sentiment')
#     logger.setLevel(logging.INFO)
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     if args.log_path:
#         file_handler = logging.FileHandler(args.log_path)
#         file_handler.setLevel(logging.INFO)
#         file_handler.setFormatter(formatter)
#         logger.addHandler(file_handler)
#     else:
#         console_handler = logging.StreamHandler()
#         console_handler.setLevel(logging.INFO)
#         console_handler.setFormatter(formatter)
#         logger.addHandler(console_handler)
#
#     logger.info('Running with args : {}'.format(args))
#
#     logger.info('Model start...')
#     test.test_phone()
#     logger.info('Model over!')



def not_first_use_function(sentence):
    svm = test.test_phone(str=sentence)
    # return str("Negative:" + str(svm[0][0]) + "   Positive:" + str(svm[0][1]))


if __name__ == '__main__':
    # run()
    # str1 = "小米手机就是个垃圾手机，难用死了"
    # str1 = "手环老是充电失败，一点也不好用"
    # str1 = "我太喜欢这个手机了，必须好评"
    str1 = "我讨厌小米手机"
    print(not_first_use_function(str1))