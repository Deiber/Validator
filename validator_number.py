#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Deiber Rincon
# date: 2019-04-09

import click


"""
    Class for initialize structure and validate entered values
"""
class NumberValidator(object):

    def __init__(self, start, end, residue):
        self.start = start
        self.end = end + 1
        self.residue = residue

        super(NumberValidator, self).__init__()


    """
        Method for check minimum number for provided serie
    """
    def _check_number(self):

        if self.start <= 0 or self.end <= 0:
            click.echo('Start/End number is not positive, ending program...')

        elif self.residue == 'n':
            """
                found_number = To return
                serie_factors = Dict for stores the factors of all numbers
            """
            found_number = 1
            serie_factors = {}
            """
                Iterating over serie
            """
            for number in range(self.start, self.end):
                """
                    divisor = The factorize starts from number 2
                    to_divide = Stores the resultant value according to factor process
                    factor_data = Stores number's factors and its quantities
                """
                divisor = 2
                to_divide = number
                number_factor = {}

                while divisor <= to_divide: # if to_divide is divisible by divisor yet
                    
                    while to_divide % divisor == 0: # if is divisible do next
                        to_divide = to_divide/divisor
                        number_factor[divisor] = number_factor.get(divisor,0)+1 # adding factor quantity

                    divisor += 1 # next divisor when to_divide is not divisible for current divisor

                """
                    Replacing factor quantity if validated factor not exist or already exists and its value is lower than validated
                """
                for key, value in number_factor.items():
                    if serie_factors.get(key,0) < value:
                        serie_factors[key] = value

            """
                Operating factors to consolidate the final number
            """
            for key, value in serie_factors.items():
                found_number *= key**value

            return found_number
                    


"""
    Using click as prompt user client
"""
@click.command()
@click.option('--start', '-s', prompt='Start of serie (default 1)', default=1, help='Start number of serie')
@click.option('--end', '-e', prompt='End of serie (default 10)', default=10, help='End of serie')
@click.option('--residue', '-r', prompt='Allow residue? y/n', default='n')
def main(start, end, residue):
    """
        Receives and send values to the class 'NumberValidation' to be validated
    """
    validator = NumberValidator(start, end, residue)
    print('Found number is: {}'.format(validator._check_number()))



"""
    main function
""" 
if __name__ == '__main__':
    main()
