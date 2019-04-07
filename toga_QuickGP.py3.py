#!/usr/bin/env python3
import toga
from toga.style.pack import *
# Author: StpircsDahc
# Author's github repo - https://github.com/stpircsdahc



def discountit(cost, discount):
    dPercentage = float(discount)/100.0
    salePrice = float(cost) - (float(cost) * dPercentage)
    salePrice = round(salePrice, 2)
    saleString = '          $ ' +str(salePrice)
    self.dPriceVar.set(saleString)
    return salePrice

def markitup(cost, markup):
    muPercentage = float(markup)/100.0
    salePrice = float(cost) + (float(cost) * muPercentage)
    salePrice = round(salePrice, 2)
    saleString = '          $ ' +str(salePrice)
    self.fPriceVar.set(saleString)
    gp = round(salePrice - cost, 2)
    gpString = '          $ ' +str(gp)
    self.gpVar.set(gpString)

def build(app):
    msrp_box = toga.Box()
    discount_box = toga.Box()
    dPrice_box = toga.Box()
    markup_box = toga.Box()
    fPrice_box = toga.Box()
    box = toga.Box()

    msrp_input = toga.TextInput()
    discount_input = toga.TextInput()
    dPrice_input = toga.TextInput(readonly=True)
    markup_input = toga.TextInput()
    fPrice_input = toga.TextInput(readonly=True)

    msrp_label = toga.Label('MSRP - List Price', style=Pack(text_align=RIGHT))
    discount_label = toga.Label('Discount Percentage', style=Pack(text_align=RIGHT))
    dPrice_label = toga.Label('Discounted sales price', style=Pack(text_align=RIGHT))
    markup_label = toga.Label('Markup Percentage', style=Pack(text_align=RIGHT))
    fPrice_label = toga.Label('Final sales price', style=Pack(text_align=RIGHT))

    def click_calc(widget):
        dPrice_input.value = 'calc button pushed'
        fPrice_input.value = 'calc button pushed'
        # if msrp_input.value and discount_input.value and markup_input.value:
        #     try:
        #         discountPrice = discountit(float(msrp_input.value), float(discount_input.value))
        #         markitup(discountPrice, markup_input.value)
        #     except:
        #         pass
        # elif self.lPrice_input.get() and self.discount_input.get():
        #     discountPrice = self.discountit(self.lPrice_input.get(), self.discount_input.get())
        # else:
        #     pass

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

    box.add(msrp_box)
    box.add(discount_box)
    box.add(dPrice_box)
    box.add(markup_box)
    box.add(fPrice_box)
    box.add(calc_button)

    box.style.update(direction=COLUMN, padding_top=10)
    msrp_box.style.update(direction=ROW, padding=5)
    discount_box.style.update(direction=ROW, padding=5)
    dPrice_box.style.update(direction=ROW, padding=5)
    markup_box.style.update(direction=ROW, padding=5)
    fPrice_box.style.update(direction=ROW, padding=5)

    msrp_input.style.update(flex=1, padding_right=60)
    discount_input.style.update(flex=1, padding_right=60)
    dPrice_input.style.update(flex=1, padding_right=60)
    markup_input.style.update(flex=1, padding_right=60)
    fPrice_input.style.update(flex=1, padding_right=60)

    msrp_label.style.update(width=200,  padding_right=10)
    discount_label.style.update(width=200,  padding_right=10)
    dPrice_label.style.update(width=200,  padding_right=10)
    markup_label.style.update(width=200,  padding_right=10)
    fPrice_label.style.update(width=200,  padding_right=10)

    calc_button.style.update(padding=15, width=100, color='#ececec')

    return box



def main():
    return toga.App('GP Calculator', 'org.stpricsdahc.GPCalc', startup=build)

if __name__ == '__main__':
    main().main_loop()
