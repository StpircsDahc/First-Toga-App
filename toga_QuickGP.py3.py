#!/usr/bin/env python3
import toga
from toga.style.pack import *
# Author: StpircsDahc
# Author's github repo - https://github.com/stpircsdahc



def discountit(cost, discount):
    print('tag tag tag')
    dPercentage = float(discount)/100.0
    salePrice = float(cost) - (float(cost) * dPercentage)
    salePrice = round(salePrice, 2)
    return salePrice

def markitup(cost, markup):
    muPercentage = float(markup)/100.0
    salePrice = float(cost) + (float(cost) * muPercentage)
    salePrice = round(salePrice, 2)
    gp = round(salePrice - cost, 2)
    return salePrice, gp

def build(app):
    msrp_box = toga.Box()
    discount_box = toga.Box()
    dPrice_box = toga.Box()
    markup_box = toga.Box()
    fPrice_box = toga.Box()
    GrossProfit_box = toga.Box()
    box = toga.Box()

    msrp_input = toga.TextInput()
    discount_input = toga.TextInput()
    dPrice_input = toga.TextInput(readonly=True)
    markup_input = toga.TextInput()
    fPrice_input = toga.TextInput(readonly=True)
    GrossProfit_input = toga.TextInput(readonly=True)

    msrp_label = toga.Label('MSRP - List Price', style=Pack(text_align=RIGHT))
    discount_label = toga.Label('Discount Percentage', style=Pack(text_align=RIGHT))
    dPrice_label = toga.Label('Discounted sales price', style=Pack(text_align=RIGHT))
    markup_label = toga.Label('Markup Percentage', style=Pack(text_align=RIGHT))
    fPrice_label = toga.Label('Final sales price', style=Pack(text_align=RIGHT))
    GrossProfit_label = toga.Label('Gross Profit', style=Pack(text_align=RIGHT))

    def click_calc(widget):
        if msrp_input.value and discount_input.value and markup_input.value:
            try:
                discountPrice = discountit(float(msrp_input.value), float(discount_input.value))
                dPrice_input.value = discountPrice
                markedupPrice, gProfit = markitup(float(discountPrice), markup_input.value)
                fPrice_input.value = markedupPrice
                GrossProfit_input.value = gProfit
            except:
                dPrice_input.value = '????'
                fPrice_input.value = '????'
                GrossProfit_input.value = '????'
        elif msrp_input.value and discount_input.value:
            try:
                discountPrice = discountit(float(msrp_input.value), float(discount_input.value))
                dPrice_input.value = discountPrice
                fPrice_input.value = 'N/A'
                GrossProfit_input.value = 'N/A'
            except:
                dPrice_input.value = '????'
                fPrice_input.value = '????'
                GrossProfit_input.value = '????'
        else:
            pass

    calc_button = toga.Button('Calculate', on_press=click_calc)

    msrp_box.add(msrp_label)
    msrp_box.add(msrp_input)

    discount_box.add(discount_label)
    discount_box.add(discount_input)

    dPrice_box.add(dPrice_label)
    dPrice_box.add(dPrice_input)

    markup_box.add(markup_label)
    markup_box.add(markup_input)

    fPrice_box.add(fPrice_label)
    fPrice_box.add(fPrice_input)

    GrossProfit_box.add(GrossProfit_label)
    GrossProfit_box.add(GrossProfit_input)

    box.add(msrp_box)
    box.add(discount_box)
    box.add(dPrice_box)
    box.add(markup_box)
    box.add(fPrice_box)
    box.add(GrossProfit_box)
    box.add(calc_button)

    box.style.update(direction=COLUMN, padding_top=10)
    msrp_box.style.update(direction=ROW, padding=5)
    discount_box.style.update(direction=ROW, padding=5)
    dPrice_box.style.update(direction=ROW, padding=5)
    markup_box.style.update(direction=ROW, padding=5)
    fPrice_box.style.update(direction=ROW, padding=5)
    GrossProfit_box.style.update(direction=ROW, padding=5)

    msrp_input.style.update(flex=1, padding_right=60)
    discount_input.style.update(flex=1, padding_right=60)
    dPrice_input.style.update(flex=1, padding_right=60)
    markup_input.style.update(flex=1, padding_right=60)
    fPrice_input.style.update(flex=1, padding_right=60)
    GrossProfit_input.style.update(flex=1, padding_right=60)

    msrp_label.style.update(width=200,  padding_right=10)
    discount_label.style.update(width=200,  padding_right=10)
    dPrice_label.style.update(width=200,  padding_right=10)
    markup_label.style.update(width=200,  padding_right=10)
    fPrice_label.style.update(width=200,  padding_right=10)
    GrossProfit_label.style.update(width=200,  padding_right=10)

    calc_button.style.update(padding=10, width=100)

    return box



def main():
    return toga.App('GP Calculator', 'org.stpricsdahc.GPCalc', startup=build)

if __name__ == '__main__':
    main().main_loop()
