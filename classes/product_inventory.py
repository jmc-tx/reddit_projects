#!/usr/bin/python
# python 3.7
# -*- coding: utf-8 -*-
# ==============================================================================
#
#         FILE: product_inventory.py
#
#        USAGE: ./product_inventory.py
#
#  DESCRIPTION: Application which manages an inventory of products.
#               Class to store price, id, and quantity on hand
#               Class to track all products and sum up total value
#
#       AUTHOR: Justen Crockett
#      VERSION: 1.0
#      CREATED: 12/05/2018
# ==============================================================================


class Product:

    def __init__(self):
        self.price = 0
        self.id = 0
        self.quantity = 0

    


class Inventory:

    def __init__(self):
        self.data = []
