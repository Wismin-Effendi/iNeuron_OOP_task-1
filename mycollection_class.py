from logging_class import Logging_CLS


class MyCollection(object):

    def __init__(self, input_data, collection_type):
        self.input_data = input_data
        self.log = Logging_CLS('collection_log001.txt').log
        self.log.info(f"Processing for collection type {collection_type}")
        try:
            if collection_type == 'list':
                self.type = list
            elif collection_type == 'tuple':
                self.type = tuple
            elif collection_type == 'set':
                self.type = set
            else:
                raise RuntimeError("Collection type must be list, tuple or set")
        except Exception as e:
            self.log.exception(e)

    def extract_collection_type(self):
        output = []
        self.log.info(f"Extracting collection from {self.input_data}")
        try:
            for e in self.input_data:
                if type(e) == self.type:
                    output.append(e)
            self.log.info(f"Result: {output}")
            return output
        except Exception as e:
            self.log.exception(e)

    def extract_number(self):
        output_numbers = []
        self.log.info(f"Extracting numbers from {self.input_data}")
        try:
            for e in self.input_data:
                if type(e) == int:
                    output_numbers.append(e)
                elif type(e) == self.type:
                    for e2 in e:
                        if type(e2) == int:
                            output_numbers.append(e2)
            self.log.info(f"Output numbers: {output_numbers}")
            return output_numbers
        except Exception as e:
            self.log.exception(e)

    def summation(self):
        """
        Sum the numerical data present in list of an input list
        :return: summation
        """
        sum = 0
        self.log.info(f"Adding number from {self.input_data}")
        try:
            for e in self.input_data:
                if type(e) == self.type:
                    for ee in e:
                        if type(ee) == int:
                            sum += ee
            self.log.info(f"Sum of the numbers = {sum}")
            return sum
        except Exception as e:
            self.log.exception(e)

    def extract_odd_numbers(self):
        try:
            odd_numbers = []
            self.log.info(f"Extract Odd numbers from input_data: {self.input_data}")
            for e in self.input_data:
                if type(e) == self.type:
                    for ee in e:
                        if type(ee) == int:
                            if ee % 2 != 0:
                                odd_numbers.append(ee)
            odd_numbers = list(set(odd_numbers))
            self.log.info(f"Odd numbers are: {odd_numbers}")
            return odd_numbers
        except Exception as e:
            self.log.exception(e)

    def occurrence(self):
        '''
        count occurrence of elements in list
        :return: dict of occurrence
        '''
        try:
            from collections import defaultdict
            counter = defaultdict(int)
            self.log.info(f"Count occurrence of Elements from input data: {self.input_data}")
            for e in self.input_data:
                if type(e) == self.type:
                    for ee in e:
                        counter[ee] += 1
            self.log.info(f"Count of occurrence: {counter}")
            return counter
        except Exception as e:
            self.log.exception(e)

    def filter_string(self):
        '''
        filter string from list
        :return: list of string
        '''
        try:
            self.log.info(f"Filtering string element from input: {self.input_data}")
            output = []
            for e in self.input_data:
                if type(e) == self.type:
                    for ee in e:
                        if type(ee) == str:
                            output.append(ee)
            self.log.info(f"String output: {output}")
            return output
        except Exception as e:
            self.log.exception(e)

    def filter_alphanumeric(self):
        '''
        Filter the alphanumeric elements in list
        :return: list
        '''
        try:
            self.log.info(f"Filter alphanumeric from input list: {self.input_data}")
            output = []
            for e in self.input_data:
                if type(e) == self.type:
                    for ee in e:
                        if type(ee) == str and ee.isalnum():
                            output.append(ee)
            self.log.info(f"Alphanumeric output: {output}")
        except Exception as e:
            self.log.exception(e)

    def multiply_elements(self):
        '''
        Multiply numeric element in each list
        :return: list of multiplication result
        '''
        try:
            output = []
            self.log.info(f"Multiply the numeric elements of the list in {self.input_data}")
            result = 1
            has_numeric = False
            for e in self.input_data:
                if type(e) == self.type:
                    for ee in e:
                        if type(ee) == int:
                            has_numeric = True
                            result *= ee
                    if has_numeric:
                        output.append(result)
                    result = 1
                    has_numeric = False
            self.log.info(f"Multiplication result: {output}")
            return output
        except Exception as e:
            self.log.exception(e)

    def run_all(self):
        self.extract_collection_type()
        self.extract_number()
        self.summation()
        self.extract_odd_numbers()
        self.occurrence()
        self.filter_string()
        self.filter_alphanumeric()
        self.multiply_elements()

