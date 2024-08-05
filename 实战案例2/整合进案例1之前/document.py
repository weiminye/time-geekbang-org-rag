class Document:
    def __init__(self):
        """
        初始化Document类，不进行字段的初始化，所有字段默认为None
        """
        self.metadata = None
        self.content = None
        self.summary = None
        self.translation = None
        self.summaryTranslation = None

    def set_metadata(self, metadata):
        """
        设置文档的元数据

        :param metadata: 文档的元数据，类型为dict
        """
        self.metadata = metadata

    def set_content(self, content):
        """
        设置文档的内容

        :param content: 文档的主要内容，类型为str
        """
        self.content = content

    def set_translation(self, translation):
        """
        设置文档的翻译版本

        :param translation: 文档的翻译版本，类型为str
        """
        self.translation = translation

    def set_summary(self, summary):
        """
        设置文档的摘要

        :param summary: 文档的摘要，类型为str
        """
        self.summary = summary

    def set_summaryTranslation(self, summaryTranslation):
        """
        设置摘要的翻译

        :param summaryTranslation: 摘要的翻译，类型为str
        """
        self.summaryTranslation = summaryTranslation
