ó
`c           @   sa  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l j Z e j e j  d' Z d( Z	 d  Z
 e a e a e a d Z d Z d   Z d   Z e j e  e e  e e	  k rÉ e e  d Z n d GHe   xJ e	 D]B Z e j e e j  e j e e j d d e j e e  qÜ Wx1 e D]) Z e j e e j  e j e e  q)Wxe r\d Z  d Z! d Z" d GHe j e d e  x- e j# e	 d  e j$ k r¹e j% d  qWx e D] Z e j e e  qÁWd GHe j% d  e j e d e  d GHe j% d  e j e d e  d GHe j% d  e j e d e  d GHe j% d  e j e d e  d GHe j% d  e j e d e  d  GHe j% d  x<e! e  k  rée a e a e a e! d 7Z! e j& d e  Z
 e j% d  e j e e
 e  e j   Z' x t e k r4e j% d!  qWe j   Z( e( e' Z) e j e e
 e  d" e) GHt r´e* d e) d d d  Z+ e+ d k  rd Z+ n  d# e+ GHe" e+ 7Z" n  t rÐd$ e GHe" e 8Z" n  d% e" GHe j% d  q®Wxl e, d d  D][ Z- xR e, d e e   D]; Z. e j e e. e  e j% d&  e j e e. e  qWqúWqYWd S()   iÿÿÿÿNi   i   i   i   i   i   i   i   i   i   i
   c         C   s2   d |  GHt  a |  t t k r( t  a n t  a d  S(   Ns   button pressed %s(   t   Truet   button_pressedt   switchest   random_numbert   correct_buttont   incorrect_button(   t   channel(    (    s   pivot_proto.pyt   buttonPress   s
    		c           C   s   d GHt  j   d  S(   Ns   GPIO Clean Up!(   t   GPIOt   cleanup(    (    (    s   pivot_proto.pyt   exit&   s    i   s/   There isn't the same number of LEDS as SWITCHESt
   bouncetimei,  i   i    s    Press the lit up button to startg{®Gáz?s   Starting in 5!g      à?s   4!s   3!i   s   2!i   s   1!i   s	   Go Go Go!g{®Gázt?s   Time taken: %fs   %f points added to your score!s#   %f points deducted from your score!s   New score: %fg¹?(   i   i   i   i   i   (   i   i   i   i   i   (/   t   syst   timet   atexitt   randomt   RPi.GPIOR   t   setmodet   BCMt   ledsR   R   t   FalseR   R   R   t
   max_pointst	   deductionR   R
   t   registert   lent   maxt   switcht   setupt   INt   add_event_detectt   RISINGt   add_event_callbackt   ledt   OUTt   outputR    t   loopt   countert   scoret   inputt   LOWt   sleept   randintt   startt   endt
   time_takent   roundt   pointst   ranget   xt   y(    (    (    s   pivot_proto.pyt   <module>   sª   			

					