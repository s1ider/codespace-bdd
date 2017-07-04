def get_ui_class(class_name, module='support.ui'):
    elements = __import__(module, fromlist=[str(class_name.lower())])
    elements_class = getattr(elements, class_name.capitalize())
    return elements_class
