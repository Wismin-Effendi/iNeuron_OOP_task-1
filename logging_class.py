class Logging_CLS:
    def __init__(self, filename, level='INFO'):
        import logging
        log_format = '%(levelname)s %(asctime)s %(name)s %(message)s'
        logging.basicConfig(filename=filename,
                            level=level,
                            format=log_format)
        self.log = logging


# Example usage:
"""
log = Logging_CLS('log0001.txt', 'INFO').log
log.error('Hello error')
log.info("hi there")
"""
