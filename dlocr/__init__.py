from dlocr.ctpn.lib.utils import get_session
from dlocr.text_detection_app import TextDetectionApp

from dlocr.ctpn import default_ctpn_weight_path, default_ctpn_config_path
from dlocr.densenet import default_densenet_weight_path, default_densenet_config_path, default_dict_path

__ocr = None


def get_or_create(ctpn_weight_path=default_ctpn_weight_path,
                  ctpn_config_path=default_ctpn_config_path,
                  densenet_weight_path=default_densenet_weight_path,
                  densenet_config_path=default_densenet_config_path,
                  dict_path=default_dict_path):
    global __ocr
    if __ocr is None:
        __ocr = TextDetectionApp(ctpn_weight_path=ctpn_weight_path,
                                 ctpn_config_path=ctpn_config_path,
                                 densenet_weight_path=densenet_weight_path,
                                 densenet_config_path=densenet_config_path,
                                 dict_path=dict_path)
    return __ocr
