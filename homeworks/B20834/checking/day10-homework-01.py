#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

#作业2: （选做）模拟下面的过程，用今天学到的知识
#【场景模拟】
#
# 老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释
# abandon “to give up to the control or influence of another person or agent”
# abase  “to lower in rank, office, prestige, or esteem ”
# abash  “to destroy the self-possession or self-confidence of ”
# 
# 老爸先查了一个单词 'etiquette' 没有查到
# 老爸怒了，把含有 'abandon' 一页的单词撕掉了
# 然后老爸又查了一个单词 'abase' 得到了解释
# 老爸很开心，又把 'abandon' 加入到了字典里
# 
# 老爸把字典翻了一遍
#   - 看到%s（单词）:%s(意思)
# 
# 第二个作业我已经做完，先不要看第二个版本

# 做几件事情
# 1. 把老爸换成老妈，做的时候数一数改了几处代码 6处
# 2. 把撕毁的页码换成'abase'，做的时候数一数改了几处代码 
# 3. 想想如何让最后粘贴回 撕毁代码页 的时候不用重复再打一遍长串释意
# 4. 如果查到就打印:'老爸查到了 %s : %s', 写代码让老爸再搜索'abase' 'abash'这两个单词
#    数一数有多少处重复的打印代码  满屏都是重复.....
# 
# 做完这些过后，打开 day10-homework2.py 做同样的事情（3除外）
def homework2():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  word = ['abandon','abase','abash']
  index = 0
  for index in range(0,len(word)):
      word[index] = book[word[index]]
      index = index + 1
  if book.has_key('etiquette'):
    print '老妈查到了%s的意思是:' % ('etiquette',book['etiquette'])
  else:
    print '老妈先查了一个单词%s没有查到' % ('etiquette')
    del book['abase']
    print '老妈怒了，把含有abase一页的单词撕掉了'
  if book.has_key('abandon'):
    print '然后老妈又查了一个单词%s得到了解释:%s' % ('abandon',book['abandon'])
    book['abase'] = word[1] 
  else:
    print '老妈没有查到abase'

    
    
  for key in book:
    print '老妈看到%s的意思是:%s' % (key,book[key])
  if book.has_key('abase'):
    print '然后老妈又查了一个单词%s得到了解释:%s' % ('abase',book['abase'])
  else:
    print '老妈没有查到abase'
  if book.has_key('abash'):
    print '然后老妈又查了一个单词%s得到了解释:%s' % ('abash',book['abash'])
  else:
    print '老妈没有查到abash'

if __name__ == '__main__':
  homework2()