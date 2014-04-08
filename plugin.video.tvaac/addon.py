#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright 2013 enen92
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,xbmc,xbmcaddon,xbmcvfs,socket,os,sys
from t0mm0.common.addon import Addon
import datetime
import time

base_url = 'http://www.rtp.pt'
img_base_url = 'http://img0.rtp.pt'
player = base_url + '/play/player.swf'
linkpart = ' live=true timeout=15'
##############Pasta de Imagens####################
addon_id = 'plugin.video.tvAAC'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id)
datapath = addon.get_profile()
addonfolder = selfAddon.getAddonInfo('path')
artfolder = '/resources/img/'
##################################################
favpath=os.path.join(datapath,'Favourites')
programafav=os.path.join(favpath,'Programa')
ADDON = selfAddon


if ADDON.getSetting('ga_visitor')=='':
    from random import randint
    ADDON.setSetting('ga_visitor',str(randint(0, 0x7fffffff)))
   
PATH = "RTPplay"  #<---- PLUGIN NAME MINUS THE "plugin.video"          
UATRACK="UA-41937813-1" #<---- GOOGLE ANALYTICS UA NUMBER  
VERSION = "1.0.9" #<---- PLUGIN VERSION

def CATEGORIES():
        ONDEMANDMENU()
        xbmc.executebuiltin("Container.SetViewMode(501)")

       


def ONDEMANDMENU():
        addDir('[COLOR blue][B]EM DIRECTO[/B][/COLOR]','Volta menu',5, addonfolder + artfolder + 'live.png','nao')
        addDir('[B]- Canais Tv/Rádio[/B]','http://www.rtp.pt/play/direto',4,addonfolder + artfolder + 'all.png','nao')
        addDir('[COLOR blue][B]EMISSÕES[/B][/COLOR]','Volta menu',5, addonfolder + artfolder + 'emissoes.png','nao')
        addDir('[B]- Mais recentes[/B]','http://www.rtp.pt/play/ondemand',8, addonfolder + artfolder + 'recentes.png','nao')
        addDir('[B]- Mais populares[/B]','http://www.rtp.pt/play/sideWidget.php?type=popular&place=HP',7, addonfolder + artfolder + 'stared.png','nao')
        addDir('[B]- Listar[/B]','http://www.rtp.pt/play/ondemand',16, addonfolder + artfolder + 'listar.png','nao')
        addDir('[B]- Pesquisar[/B]','http://www.rtp.pt/play/ondemand',21, addonfolder + artfolder + 'pesquisar.png','nao')
        addDir('[COLOR blue][B]PROGRAMAS[/B][/COLOR]','Volta menu',5, addonfolder + artfolder + 'programas.png','nao')
        addDir('[B]- Favoritos[/B]','http://www.rtp.pt/play/ondemand',25, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]- De A-Z[/B]','http://www.rtp.pt/play/ondemand',12, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]- Pesquisar[/B]','http://www.rtp.pt/play/ondemand',22,addonfolder + artfolder + 'pesquisar.png','nao')
        GA("None","Menu inicial")


def LIVEMENU():
        addDir('[B]TV[/B]','http://www.rtp.pt/play/direto/tv',4,addonfolder + artfolder + 'tv.png','nao')
        addDir('[B]Rádio[/B]','http://www.rtp.pt/play/direto/radio',4,addonfolder + artfolder + 'radio.png','nao')
        addDir('[B]Todos[/B]','http://www.rtp.pt/play/direto',4,addonfolder + artfolder + 'all.png','nao')

def RECENTESMENU():
        addDir('[B]- Emissoões da TV[/B]','http://www.rtp.pt/play/recent.php?type=TV',9, addonfolder + artfolder + 'tv.png','nao')
        addDir('[B]- Emissões da rádio[/B]','http://www.rtp.pt/play/recent.php?type=RADIO',9, addonfolder + artfolder + 'radio.png','nao')
        GA("None","Emissoes recente listar menu")

def AZMENU():
        addDir('[B]- Emissões da TV[/B]','http://www.rtp.pt/play/recent.php?type=TV',13, addonfolder + artfolder + 'tv.png','nao')
        addDir('[B]- Emissões da Rádio[/B]','http://www.rtp.pt/play/recent.php?type=RADIO',14, addonfolder + artfolder + 'radio.png','nao')
        GA("None","Programa listar menu")

def TVAZMENU():
        addDir('[B]#[/B]','http://www.rtp.pt/play/az.php?letter=0-9&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]A[/B]','http://www.rtp.pt/play/az.php?letter=A&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]B[/B]','http://www.rtp.pt/play/az.php?letter=B&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]C[/B]','http://www.rtp.pt/play/az.php?letter=C&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]D[/B]','http://www.rtp.pt/play/az.php?letter=D&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]E[/B]','http://www.rtp.pt/play/az.php?letter=E&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]F[/B]','http://www.rtp.pt/play/az.php?letter=F&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]G[/B]','http://www.rtp.pt/play/az.php?letter=G&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]H[/B]','http://www.rtp.pt/play/az.php?letter=H&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]I[/B]','http://www.rtp.pt/play/az.php?letter=I&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]J[/B]','http://www.rtp.pt/play/az.php?letter=J&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]K[/B]','http://www.rtp.pt/play/az.php?letter=K&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]L[/B]','http://www.rtp.pt/play/az.php?letter=L&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]M[/B]','http://www.rtp.pt/play/az.php?letter=M&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]N[/B]','http://www.rtp.pt/play/az.php?letter=N&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]O[/B]','http://www.rtp.pt/play/az.php?letter=O&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]P[/B]','http://www.rtp.pt/play/az.php?letter=P&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]Q[/B]','http://www.rtp.pt/play/az.php?letter=Q&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]R[/B]','http://www.rtp.pt/play/az.php?letter=R&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]S[/B]','http://www.rtp.pt/play/az.php?letter=S&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]T[/B]','http://www.rtp.pt/play/az.php?letter=T&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]U[/B]','http://www.rtp.pt/play/az.php?letter=U&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]V[/B]','http://www.rtp.pt/play/az.php?letter=V&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]W[/B]','http://www.rtp.pt/play/az.php?letter=W&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]X[/B]','http://www.rtp.pt/play/az.php?letter=X&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]Y[/B]','http://www.rtp.pt/play/az.php?letter=Y&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]Z[/B]','http://www.rtp.pt/play/az.php?letter=Z&channelType=tv',15, addonfolder + artfolder + 'programasaz.png','nao')
        GA("None","Tv az menu")

def RADIOAZMENU():
        addDir('[B]#[/B]','http://www.rtp.pt/play/az.php?letter=0-9&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]A[/B]','http://www.rtp.pt/play/az.php?letter=A&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]B[/B]','http://www.rtp.pt/play/az.php?letter=B&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]C[/B]','http://www.rtp.pt/play/az.php?letter=C&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]D[/B]','http://www.rtp.pt/play/az.php?letter=D&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]E[/B]','http://www.rtp.pt/play/az.php?letter=E&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]F[/B]','http://www.rtp.pt/play/az.php?letter=F&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]G[/B]','http://www.rtp.pt/play/az.php?letter=G&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]H[/B]','http://www.rtp.pt/play/az.php?letter=H&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]I[/B]','http://www.rtp.pt/play/az.php?letter=I&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]J[/B]','http://www.rtp.pt/play/az.php?letter=J&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]K[/B]','http://www.rtp.pt/play/az.php?letter=K&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]L[/B]','http://www.rtp.pt/play/az.php?letter=L&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]M[/B]','http://www.rtp.pt/play/az.php?letter=M&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]N[/B]','http://www.rtp.pt/play/az.php?letter=N&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]O[/B]','http://www.rtp.pt/play/az.php?letter=O&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]P[/B]','http://www.rtp.pt/play/az.php?letter=P&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]Q[/B]','http://www.rtp.pt/play/az.php?letter=Q&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]R[/B]','http://www.rtp.pt/play/az.php?letter=R&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]S[/B]','http://www.rtp.pt/play/az.php?letter=S&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]T[/B]','http://www.rtp.pt/play/az.php?letter=T&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]U[/B]','http://www.rtp.pt/play/az.php?letter=U&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]V[/B]','http://www.rtp.pt/play/az.php?letter=V&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]W[/B]','http://www.rtp.pt/play/az.php?letter=W&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]X[/B]','http://www.rtp.pt/play/az.php?letter=X&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]Y[/B]','http://www.rtp.pt/play/az.php?letter=Y&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        addDir('[B]Z[/B]','http://www.rtp.pt/play/az.php?letter=Z&channelType=radio',15, addonfolder + artfolder + 'programasaz.png','nao')
        GA("None","radio menu az")

def EMISSAOLISTARMENU():
        addDir('[B]- Por canal[/B]','http://www.rtp.pt/play/ondemand',17, addonfolder + artfolder + 'emissoes.png','nao')
        addDir('[B]- Por tema[/B]','http://www.rtp.pt/play/ondemand',18, addonfolder + artfolder + 'emissoes.png','nao')
        GA("None","Emissao listar menu")

def EMISSAOLISTARMENU_CANAL(url):
        link = abrir_url(url)
        match=re.compile('<a href="/play/procura\?p_c=(.+?)" title=".+?">(.+?)</a>').findall(link)
        for canal,titulo in match:
                titulo = titulo.replace('&uacute;', "ú");
                titulo = titulo.replace('&ccedil;', "ç");
                titulo = titulo.replace('&atilde;', "ã");
                titulo = titulo.replace('&ecirc;', "ê");
                titulo = titulo.replace('&oacute;', "ó");
                titulo = titulo.replace('&Aacute;', "Á");
                addDir('[B]' + titulo + '[/B]',base_url + '/play/procura?p_c=' + canal,19, addonfolder + artfolder + 'emissoes.png','nao')
        GA("None","emissoes por canal")


def EMISSAOLISTARMENU_TEMA(url):
        link = abrir_url(url)
        match=re.compile('<a href="/play/procura\?p_t=(.+?)" title=".+?">(.+?)</a>').findall(link)
        for tema,titulo in match:
                titulo = titulo.replace('&uacute;', "ú");
                titulo = titulo.replace('&ccedil;', "ç");
                titulo = titulo.replace('&atilde;', "ã");
                titulo = titulo.replace('&ecirc;', "ê");
                titulo = titulo.replace('&oacute;', "ó");
                titulo = titulo.replace('&Aacute;', "Á");
                addDir('[B]' + titulo + '[/B]',base_url + '/play/procura?p_t=' + tema,19, addonfolder + artfolder + 'emissoes.png','nao')
        GA("None","emissao listar menu por tema")
       

def LIVEFUNCTION(url):
        link = abrir_url(url)
        match=re.compile('<a  id=".+?" title="(.+?)" href="(.+?)"><img src="(.+?)"').findall(link)
        print match
        for titulo,url2,img in match:
                titulo = titulo.replace('&uacute;', "ú");
                titulo = titulo.replace('&ccedil;', "ç");
                titulo = titulo.replace('&atilde;', "ã");
                titulo = titulo.replace('&acirc;', "â");
                titulo = titulo.replace('&ecirc;', "ê");
                titulo = titulo.replace('&oacute;', "ó");
                titulo = titulo.replace('&Oacute;', "Ó");
                titulo = titulo.replace('&Aacute;', "Á");
                titulo = titulo.replace('&aacute;', "á");
                STREAMER('[B][COLOR blue]' + titulo + '[/B][/COLOR]',base_url + url2,img)
        match=re.compile('<a id=".+?" title="(.+?)" href="(.+?)"><img src="(.+?)"').findall(link)
        print match
        for titulo,url2,img in match:
                titulo = titulo.replace('&uacute;', "ú");
                titulo = titulo.replace('&ccedil;', "ç");
                titulo = titulo.replace('&atilde;', "ã");
                titulo = titulo.replace('&acirc;', "â");
                titulo = titulo.replace('&ecirc;', "ê");
                titulo = titulo.replace('&oacute;', "ó");
                titulo = titulo.replace('&Oacute;', "Ó");
                titulo = titulo.replace('&Aacute;', "Á");
                titulo = titulo.replace('&aacute;', "á");
                STREAMER('[B][COLOR blue]' + titulo + '[/B][/COLOR]',base_url + url2,img)
        xbmc.executebuiltin("Container.SetViewMode(500)")
        GA("None","Canais em Directo")
       

def STREAMER(name,url,img):
        link = abrir_url(url)
        if re.search('mms:', link):
                match=re.compile('\"file\": \"(.+?)\",\"streamer\": \"(.+?)\"').findall(link)
                url2 = match[0][1] + match[0][0]
                addLink(name,url2,img)
        else:
                tipostr=selfAddon.getSetting('tipostr')
                print tipostr + 'tipo'
                if tipostr == '0':
                        if xbmc.getCondVisibility('system.platform.OSX') == True: versao = 'rtmp'
                        elif xbmc.getCondVisibility('system.platform.IOS') == True: versao = 'm3u8'
                        elif xbmc.getCondVisibility('system.platform.ATV2') == True: versao = 'm3u8'            
                        elif xbmc.getCondVisibility('system.platform.Windows') == True: versao = 'rtmp'
                        elif xbmc.getCondVisibility('system.platform.linux') == True:
                                archit = os.uname()[4]                  
                                archit.find('armv6l')
                                if archit.find('armv6l') == -1: versao = 'rtmp'
                                else: versao = 'm3u8'
                elif tipostr == '1': versao = 'rtmp'
                elif tipostr == '2': versao = 'm3u8'


                if versao == 'rtmp':
                        match=re.compile('\"file\": \"(.+?)\",\"application\": \"(.+?)\",\"streamer\": \"(.+?)\"').findall(link)
                        url2 = 'rtmp://' + match[0][2] +'/' + match[0][1] + '/' + match[0][0] + ' swfUrl=' + player + linkpart
                        addLink(name,url2,img)
                else:
                        match=re.compile('\"smil\":\"(.+?)\"').findall(link)
                        url2 = match[0]
                        addLink(name,url2,img)
       

def STREAMER_DEMAND(name,url,img):
        link = abrir_url(url)
        link2=link.replace('"mp4":0', "--");
        if re.search('<b>Parte</b>2', link2):
                addDir(name,url,23,img,'')
        else:
                if re.search('mms:', link2):
                        match=re.compile('\"file\": \"(.+?)\",\"streamer\": \"(.+?)\"').findall(link2)
                        url2 = match[0][1] + match[0][0]
                        addLink(name,url2,img)
                elif re.search('.flv', link2):
                        match=re.compile('"file": "(.+?)","image": "(.+?)","application": "(.+?)","streamer": "(.+?)"').findall(link2)
                        url2 = 'rtmp://' + match[0][3] +'/' + match[0][2] + ' playpath=flv:' + match[0][0]
                        addLink(name,url2,img)
                elif re.search('.*mp4', link2):
                        match=re.compile('"file": "(.+?)","image": "(.+?)","application": "(.+?)","streamer": "(.+?)"').findall(link2)
                        url2 = 'rtmp://' + match[0][3] +'/' + match[0][2] + ' playpath=mp4:' + match[0][0]
                        addLink(name,url2,img)
                elif re.search('mp3', link2):
                        match=re.compile('"file": "(.+?)","application": "(.+?)","streamer": "(.+?)"').findall(link2)
                        url2 = 'rtmp://' + match[0][2] +'/' + match[0][1] + ' playpath=mp3:' + match[0][0]
                        addLink(name,url2,img)


def programa_paginicial(url,page_logical):
        if page_logical == '0':
                page_num = '1'
                prog_id=re.compile('http://www.rtp.pt/play/p(.+?)/').findall(url)
                url='http://www.rtp.pt/play/browseprog/' + prog_id[0] + '/' + page_num + '/true'
                link = abrir_url(url)
                match=re.compile('href="(.+?)"><img alt="(.+?)" src="(.+?)"><i class="date"><b>(.+?)</b>').findall(link)
                pag_num_total=re.compile('.*page:(.+?)}\)\">Fim &raquo').findall(link)
                for urlsbase,titulo,thumbtmp,data in match:
                        thumbtmp2=re.compile('src=(.+?)&amp').findall(thumbtmp)
                        thumbnail=img_base_url + thumbtmp2[0]
                        STREAMER_DEMAND('[B][COLOR blue]' + data + '[/B][/COLOR]',base_url + urlsbase,thumbnail)
                if pag_num_total == []:
                        pass
                else:
                        botaoseguinte(page_num,pag_num_total[0],prog_id[0])
                xbmc.executebuiltin("Container.SetViewMode(500)")
        else:
                link = abrir_url(url)
                match=re.compile('href="(.+?)"><img alt="(.+?)" src="(.+?)"><i class="date"><b>(.+?)</b>').findall(link)
                pag_num_total=re.compile('.*page:(.+?)}\)\">Fim &raquo').findall(link)
                logical_array=re.compile('http://www.rtp.pt/play/browseprog/(.+?)/(.+?)/').findall(url)
                prog_id = logical_array[0][0]
                page_num = logical_array[0][1]
                for urlsbase,titulo,thumbtmp,data in match:
                        thumbtmp2=re.compile('src=(.+?)&amp').findall(thumbtmp)
                        thumbnail=img_base_url + thumbtmp2[0]
                        STREAMER_DEMAND('[B][COLOR blue]' + data + '[/B][/COLOR]',base_url + urlsbase,thumbnail)
                if pag_num_total == []:
                        pass
                else:
                        botaoseguinte(page_num,pag_num_total[0],prog_id)
                xbmc.executebuiltin("Container.SetViewMode(500)")
                GA("None","Abriu um programa")

def botaoseguinte(page_num,pag_num_total,prog_id):
        page_next =  int(page_num) + 1
        url='http://www.rtp.pt/play/browseprog/' + prog_id + '/' + str(page_next) + '/true'
        addDir('[B]Pag '+ page_num + '/' + pag_num_total + '[/B][B][COLOR blue] | Seguinte >>[/B][/COLOR]',url,11,'','nao')

def azfunction(name,url):
        link = abrir_url(url)
        match=re.compile('href="(.+?)" title="(.+?)"><h3>(.+?)</h3>').findall(link)
        for urlsbase,merda,titulo in match:
                titulo = titulo.replace('\xc3', "Ã");
                titulo = titulo.replace('\xd3', "Ó");
                titulo = titulo.replace('\xda', "Ú");
                titulo = titulo.replace('\xca', "Ê");
                titulo = titulo.replace('\xc9', "É");
                titulo = titulo.replace('\xc7', "Ç");
                titulo = titulo.replace('\xcd', "Í");
                titulo = titulo.replace('\xc2', "Â");
                titulo = titulo.replace('\xc1', "Á");
                titulo = titulo.replace('\xc0', "À");
                titulo = titulo.replace('\xe9', "é");
                titulo = titulo.replace('\xed', "í");
                titulo = titulo.replace('\xf3', "ó");
                titulo = titulo.replace('\xe7', "ç");
                titulo = titulo.replace('\xe3', "ã");
                titulo = titulo.replace('\xe2', "â");
                titulo = titulo.replace('\xea', "ê");
                titulo = titulo.replace('\xe1', "á");
                titulo = titulo.replace('\xfa', "ú");
                titulo = titulo.replace('\xe0', "à");
                azfunction_thumb('[B][COLOR blue]'+ titulo + '[/B][/COLOR]',base_url + urlsbase)
        GA("None","abriu uma letra")


def azfunction_thumb(titulo,url):
        link = abrir_url(url)
        match=re.compile('src="(.+?)" />\s*<p class="Sinopse">',re.MULTILINE).findall(link)
        if match == []:
                thumbtmp = ''
        else:
                thumbtmp = match[0]
                thumbtmp2=re.compile('src=(.+?)&amp').findall(thumbtmp)
                thumbnail=img_base_url + thumbtmp2[0]
        addDir_programa(titulo,url,10,thumbnail,'nao')
       
def programa_emissoes(urltmp,page_logical):
        if page_logical == '0':
                page_num = '1'
                url= urltmp + '&page=' + page_num
                link = abrir_url(url)
                match=re.compile('<a href="(.+?)" title="(.+?)">\s*<img alt=".+?" src="(.+?)"').findall(link)
                pag_num_total=re.compile('.*page=(.+?)">Fim &raquo').findall(link)
                for urlsbase,titulo,thumbtmp in match:
                        thumbtmp2=re.compile('src=(.+?)&amp').findall(thumbtmp)
                        thumbnail=img_base_url + thumbtmp2[0]
                        titulo = titulo.replace('\xc3', "Ã");
                        titulo = titulo.replace('\xd3', "Ó");
                        titulo = titulo.replace('\xda', "Ú");
                        titulo = titulo.replace('\xca', "Ê");
                        titulo = titulo.replace('\xc9', "É");
                        titulo = titulo.replace('\xc7', "Ç");
                        titulo = titulo.replace('\xcd', "Í");
                        titulo = titulo.replace('\xc2', "Â");
                        titulo = titulo.replace('\xc1', "Á");
                        titulo = titulo.replace('\xc0', "À");
                        titulo = titulo.replace('\xe9', "é");
                        titulo = titulo.replace('\xed', "í");
                        titulo = titulo.replace('\xf3', "ó");
                        titulo = titulo.replace('\xe7', "ç");
                        titulo = titulo.replace('\xe3', "ã");
                        titulo = titulo.replace('\xe2', "â");
                        titulo = titulo.replace('\xea', "ê");
                        titulo = titulo.replace('\xe1', "á");
                        titulo = titulo.replace('\xfa', "ú");
                        titulo = titulo.replace('\xe0', "à");
                        STREAMER_DEMAND('[B][COLOR blue]' + titulo + '[/B][/COLOR]',base_url + urlsbase,thumbnail)
                if pag_num_total == []:
                        pass
                else:
                        botaoseguinte_emissoes(page_num,pag_num_total[0],urltmp)
                xbmc.executebuiltin("Container.SetViewMode(500)")
        else:
                link = abrir_url(urltmp)
                match=re.compile('<a href="(.+?)" title="(.+?)">\s*<img alt=".+?" src="(.+?)"').findall(link)
                pag_num_total=re.compile('.*page=(.+?)">Fim &raquo').findall(link)
                logical_array=re.compile('&page=(.+?)').findall(urltmp)
                page_num = logical_array[0][0]
                for urlsbase,titulo,thumbtmp in match:
                        thumbtmp2=re.compile('src=(.+?)&amp').findall(thumbtmp)
                        thumbnail=img_base_url + thumbtmp2[0]
                        titulo = titulo.replace('\xc3', "Ã");
                        titulo = titulo.replace('\xd3', "Ó");
                        titulo = titulo.replace('\xda', "Ú");
                        titulo = titulo.replace('\xca', "Ê");
                        titulo = titulo.replace('\xc9', "É");
                        titulo = titulo.replace('\xc7', "Ç");
                        titulo = titulo.replace('\xcd', "Í");
                        titulo = titulo.replace('\xc2', "Â");
                        titulo = titulo.replace('\xc1', "Á");
                        titulo = titulo.replace('\xc0', "À");
                        titulo = titulo.replace('\xe9', "é");
                        titulo = titulo.replace('\xed', "í");
                        titulo = titulo.replace('\xf3', "ó");
                        titulo = titulo.replace('\xe7', "ç");
                        titulo = titulo.replace('\xe3', "ã");
                        titulo = titulo.replace('\xe2', "â");
                        titulo = titulo.replace('\xea', "ê");
                        titulo = titulo.replace('\xe1', "á");
                        titulo = titulo.replace('\xfa', "ú");
                        titulo = titulo.replace('\xe0', "à");
                        STREAMER_DEMAND('[B][COLOR blue]' + titulo + '[/B][/COLOR]',base_url + urlsbase,thumbnail)
                if pag_num_total == []:
                        pass
                else:
                        botaoseguinte_emissoes(page_num,pag_num_total[0],urltmp)
                xbmc.executebuiltin("Container.SetViewMode(500)")


def botaoseguinte_emissoes(page_num,pag_num_total,urltmp):
        page_next =  int(page_num) + 1
        url=urltmp + '&page=' + str(page_next)
        addDir('[B]Pag '+ page_num + '/' + pag_num_total + '[/B][B][COLOR blue] | Seguinte >>[/B][/COLOR]',url,20,'','nao')



def POPULARES(url):
        link = abrir_url(url)
        match=re.compile('href="(.+?)"><img alt="(.+?)" src="(.+?)" /><i class="date"><b>(.+?)</b>').findall(link)
        for urlsbase,titulo,thumbtmp,data in match:
                thumbtmp2=re.compile('src=(.+?)&amp').findall(thumbtmp)
                thumbnail=img_base_url + thumbtmp2[0]
                titulo = titulo.replace('\xc3', "Ã");
                titulo = titulo.replace('\xd3', "Ó");
                titulo = titulo.replace('\xda', "Ú");
                titulo = titulo.replace('\xca', "Ê");
                titulo = titulo.replace('\xc9', "É");
                titulo = titulo.replace('\xc7', "Ç");
                titulo = titulo.replace('\xcd', "Í");
                titulo = titulo.replace('\xc2', "Â");
                titulo = titulo.replace('\xc1', "Á");
                titulo = titulo.replace('\xc0', "À");
                titulo = titulo.replace('\xe9', "é");
                titulo = titulo.replace('\xed', "í");
                titulo = titulo.replace('\xf3', "ó");
                titulo = titulo.replace('\xe7', "ç");
                titulo = titulo.replace('\xe3', "ã");
                titulo = titulo.replace('\xe2', "â");
                titulo = titulo.replace('\xea', "ê");
                titulo = titulo.replace('\xe1', "á");
                titulo = titulo.replace('\xfa', "ú");
                titulo = titulo.replace('\xe0', "à");
                STREAMER_DEMAND('[B][COLOR blue]' + titulo + '[/COLOR][/B][B]' + '-' + data + '[/B]',base_url + urlsbase,thumbnail)
        xbmc.executebuiltin("Container.SetViewMode(500)")
        GA("None","emissoes populares")

def RECENTES(url):
        link = abrir_url(url)
        match=re.compile('href="(.+?)"><img alt="(.+?)" src="(.+?)".s*/><i class="date"><b>(.+?)</b>').findall(link)
        for urlsbase,titulo,thumbtmp,date in match:
                thumbtmp2=re.compile('src=(.+?)&amp').findall(thumbtmp)
                thumbnail=img_base_url + thumbtmp2[0]
                titulo = titulo.replace('\xc3', "Ã");
                titulo = titulo.replace('\xd3', "Ó");
                titulo = titulo.replace('\xda', "Ú");
                titulo = titulo.replace('\xca', "Ê");
                titulo = titulo.replace('\xc9', "É");
                titulo = titulo.replace('\xc7', "Ç");
                titulo = titulo.replace('\xcd', "Í");
                titulo = titulo.replace('\xc2', "Â");
                titulo = titulo.replace('\xc1', "Á");
                titulo = titulo.replace('\xc0', "À");
                titulo = titulo.replace('\xe9', "é");
                titulo = titulo.replace('\xed', "í");
                titulo = titulo.replace('\xf3', "ó");
                titulo = titulo.replace('\xe7', "ç");
                titulo = titulo.replace('\xe3', "ã");
                titulo = titulo.replace('\xe2', "â");
                titulo = titulo.replace('\xea', "ê");
                titulo = titulo.replace('\xe1', "á");
                titulo = titulo.replace('\xfa', "ú");
                titulo = titulo.replace('\xe0', "à");
                STREAMER_DEMAND('[B][COLOR blue]' + titulo + '[/B][/COLOR]'+'[B]-'+ date + '[/B]',base_url + urlsbase,thumbnail)
        xbmc.executebuiltin("Container.SetViewMode(500)")
        GA("None","emissoes recentes")

               
def pesquisa_emissoes():
        keyb = xbmc.Keyboard('', 'Escreva o parâmetro de pesquisa')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
                pesquisa_emissoes_resultados(encode)  
        GA("None","Pesquisa de emissoes")              

def pesquisa_emissoes_resultados(encode):
        urltmp = base_url + '/play/procura?p_az=&p_c=&p_t=&p_d=&p_n=' + encode + '&pesquisar=OK'
        programa_emissoes(urltmp,'0')

def pesquisa_programas():
        keyb = xbmc.Keyboard('', 'Escreva o parâmetro de pesquisa')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
                pesquisa_programas_resultados(encode)  
        GA("None","Pesquisa programas")

def pesquisa_programas_resultados(encode):
        urltmp = base_url + '/play/procura?p_az=&p_c=&p_t=&p_d=&p_n=' + encode + '&pesquisar=OK'
        programa_programas(urltmp)

def programa_programas(url):
        link = abrir_url(url)
        match=re.compile('<a href="(.+?)" title=".+?"><h3>(.+?)</h3>').findall(link)
        print match
        for urlsbase,titulo in match:
                titulo = titulo.replace('\xc3', "Ã");
                titulo = titulo.replace('\xd3', "Ó");
                titulo = titulo.replace('\xda', "Ú");
                titulo = titulo.replace('\xca', "Ê");
                titulo = titulo.replace('\xc9', "É");
                titulo = titulo.replace('\xc7', "Ç");
                titulo = titulo.replace('\xcd', "Í");
                titulo = titulo.replace('\xc2', "Â");
                titulo = titulo.replace('\xc1', "Á");
                titulo = titulo.replace('\xc0', "À");
                titulo = titulo.replace('\xe9', "é");
                titulo = titulo.replace('\xed', "í");
                titulo = titulo.replace('\xf3', "ó");
                titulo = titulo.replace('\xe7', "ç");
                titulo = titulo.replace('\xe3', "ã");
                titulo = titulo.replace('\xe2', "â");
                titulo = titulo.replace('\xea', "ê");
                titulo = titulo.replace('\xe1', "á");
                titulo = titulo.replace('\xfa', "ú");
                titulo = titulo.replace('\xe0', "à");
                link = abrir_url(base_url + urlsbase)
                match=re.compile('src="(.+?)" />\s*<p class="Sinopse">',re.MULTILINE).findall(link)
                if match == []:
                        thumbtmp = ''
                else:
                        thumbtmp = match[0]
                        thumbtmp2=re.compile('src=(.+?)&amp').findall(thumbtmp)
                        thumbnail=img_base_url + thumbtmp2[0]
                addDir_programa('[B][COLOR blue]' + titulo + '[/B][/COLOR]',base_url + urlsbase,10,thumbnail,'nao')    


def play_lista(url,name):
        dp = xbmcgui.DialogProgress()
        dp.create("RTP Play",'Modo playlist')
        dp.update(0)
        playlist = xbmc.PlayList(1)
        playlist.clear()
        link2 = abrir_url(url)
        if re.search('mms:', link2):
                match=re.compile('\"file\": \"(.+?)\",\"streamer\": \"(.+?)\"').findall(link2)
                url2 = match[0][1] + match[0][0]
                liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage='')
                liz.setInfo('Video', {})
                liz.setProperty('mimetype', 'video')                
                playlist.add(url2, liz)
                addLink(name + '[B] - Parte 1[/B]',url2,'')
        elif re.search('.flv', link2):
                match=re.compile('"file": "(.+?)","image": "(.+?)","application": "(.+?)","streamer": "(.+?)"').findall(link2)
                url2 = 'rtmp://' + match[0][3] +'/' + match[0][2] + ' playpath=flv:' + match[0][0]
                liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage='')
                liz.setInfo('Video', {})
                liz.setProperty('mimetype', 'video')                
                playlist.add(url2, liz)
                addLink(name + '[B] - Parte 1[/B]',url2,'')
        elif re.search('.*mp4', link2):
                match=re.compile('"file": "(.+?)","image": "(.+?)","application": "(.+?)","streamer": "(.+?)"').findall(link2)
                url2 = 'rtmp://' + match[0][3] +'/' + match[0][2] + ' playpath=mp4:' + match[0][0]
                liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage='')
                liz.setInfo('Video', {})
                liz.setProperty('mimetype', 'video')                
                playlist.add(url2, liz)
                addLink(name + '[B] - Parte 1[/B]',url2,'')
        elif re.search('mp3'):
                match=re.compile('"file": "(.+?)","application": "(.+?)","streamer": "(.+?)"').findall(link2)
                url2 = 'rtmp://' + match[0][2] +'/' + match[0][1] + ' playpath=mp3:' + match[0][0]
                liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage='')
                liz.setInfo('Video', {})
                liz.setProperty('mimetype', 'video')                
                playlist.add(url2, liz)
                addLink(name + '[B] - Parte 1[/B]',url2,'')
        match = re.compile('.*href=\'(.+?)\'><b>Parte</b>2').findall(link2)
        link2 = abrir_url(base_url + match[0])
        if re.search('mms:', link2):
                match=re.compile('\"file\": \"(.+?)\",\"streamer\": \"(.+?)\"').findall(link2)
                url2 = match[0][1] + match[0][0]
                liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage='')
                liz.setInfo('Video', {})
                liz.setProperty('mimetype', 'video')                
                playlist.add(url2, liz)
                addLink(name + '[B] - Parte 2[/B]',url2,'')
        elif re.search('.flv', link2):
                match=re.compile('"file": "(.+?)","image": "(.+?)","application": "(.+?)","streamer": "(.+?)"').findall(link2)
                url2 = 'rtmp://' + match[0][3] +'/' + match[0][2] + ' playpath=flv:' + match[0][0]
                liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage='')
                liz.setInfo('Video', {})
                liz.setProperty('mimetype', 'video')                
                playlist.add(url2, liz)
                addLink(name + '[B] - Parte 2[/B]',url2,'')
        elif re.search('.*mp4', link2):
                match=re.compile('"file": "(.+?)","image": "(.+?)","application": "(.+?)","streamer": "(.+?)"').findall(link2)
                url2 = 'rtmp://' + match[0][3] +'/' + match[0][2] + ' playpath=mp4:' + match[0][0]
                liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage='')
                liz.setInfo('Video', {})
                liz.setProperty('mimetype', 'video')                
                playlist.add(url2, liz)
                addLink(name + '[B] - Parte 2[/B]',url2,'')
        elif re.search('mp3'):
                match=re.compile('"file": "(.+?)","application": "(.+?)","streamer": "(.+?)"').findall(link2)
                url2 = 'rtmp://' + match[0][2] +'/' + match[0][1] + ' playpath=mp3:' + match[0][0]
                liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage='')
                liz.setInfo('Video', {})
                liz.setProperty('mimetype', 'video')                
                playlist.add(url2, liz)
                addLink(name + '[B] - Parte 2[/B]',url2,'')
        dp.update(1, 'A adicionar à playlist.')
        if dp.iscanceled(): return
        dp.close()
        xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
        xbmcPlayer.play(playlist)
        GA("None","Modo playlist")

def FAVORITOS_PROGRAMAS():
        GA("None","Favoritos")
        favpath=os.path.join(datapath,'Favourites')
        programafav=os.path.join(favpath,'Programa')
        print programafav
        try:
                programasdircontents=os.listdir(programafav)
        except:
                programasdircontents=None
 
        if programasdircontents == None:
                xbmc.executebuiltin("XBMC.Notification("+"RTP Play"+","+"Nao tem programas favoritos"+","+"6000"+","")")
        else:
                print programasdircontents
                i=0
                while i < len(programasdircontents):
                        try:
                                print programafav + programasdircontents[i]
                                f = open(programafav + '/'+ programasdircontents[i], "r")
                                string = f.read()
                                print string
                                match = re.compile('(.+?)\|(.+?)\|(.+?)\|').findall(string)
                                print match
                                for name, url, img in match:
                                        addDir_programa('[B][COLOR blue]' + name + '[/B][/COLOR]',url,10,img,'programa')        
                                f.close()
                                i += 1
                        except:
                                i += 1
                                pass
                       

def REMOVER_PROGRAMAS_FAVORITO(name):
        print name
        savepath = programafav
        NewFavFile=os.path.join(savepath,name.lower()+'.txt')
        print NewFavFile
        os.remove(NewFavFile)
        xbmc.executebuiltin("XBMC.Notification("+"RTP Play"+","+"Programa removido dos favoritos"+","+"6000"+","")")
        xbmc.executebuiltin("XBMC.Container.Refresh")

############################################################################################################################

def abrir_url(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link


def ADD_TO_FAVOURITES(name,url,iconimage,checker):
        print 'Adicionando aos favoritos: name: %s, tipo: %s, url: %s' % (name, checker, url)
        favpath=os.path.join(datapath,'Favourites')
        emissaofav=os.path.join(favpath,'Emissao')
        programafav=os.path.join(favpath,'Programa')

        try:
                os.makedirs(emissaofav)
        except:
                pass
        try:
                os.makedirs(programafav)
        except:
                pass
        if checker == 'emissao':
                savepath = emissaofav
        elif checker == 'programa':
                savepath = programafav
       
        name = name.replace('[b]','')
        name = name.replace('[/b]','')
        name = name.replace('[color blue]','')
        name = name.replace('[/color]','')
        print 'o nome e',name
        NewFavFile=os.path.join(savepath,name+'.txt')
        if not os.path.exists(NewFavFile):
                favcontents=name+'|'+url+'|'+iconimage+'|'
                save(NewFavFile,favcontents)
                xbmc.executebuiltin("XBMC.Notification("+name+","+"adicionado aos favoritos"+","+"6000"+","")")
                xbmc.executebuiltin("XBMC.Container.Refresh")
        else:
                print 'Aviso - favorito ja existe'
                xbmc.executebuiltin("XBMC.Notification("+name+","+"ja esta nos favoritos"+","+"6000"+","")")
        GA("None","Adicionar aos favoritos")


             
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                               
        return param


def save(filename,contents):  
     fh = open(filename, 'w')
     fh.write(contents)  
     fh.close()



def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', addonfolder + artfolder + 'fanart.png')
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok

def addLink1(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', addonfolder + artfolder + 'fanart.png')
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        contextMenuItems = []
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok


def addDir(name,url,mode,iconimage,checker):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&checker="+urllib.quote_plus(checker)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', addonfolder + artfolder + 'fanart.png')
        liz.setInfo( type="Video", infoLabels={ "Title": name })
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addDir_programa(name,url,mode,iconimage,checker):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&checker="+urllib.quote_plus(checker)+"&iconimage="+urllib.quote_plus(iconimage)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', addonfolder + artfolder + 'fanart.png')
        liz.setInfo( type="Video", infoLabels={ "Title": name })
        contextMenuItems = []
        savepath = programafav
        name2 = name.replace('[B]','')
        name2 = name2.replace('[/B]','')
        name2 = name2.replace('[COLOR blue]','')
        name2 = name2.replace('[/COLOR]','')
        print name2
        print savepath
        NewFavFile=os.path.join(savepath,name2.lower()+'.txt')
        print NewFavFile
        if os.path.exists(NewFavFile):
                contextMenuItems.append(('Remover programa dos favoritos', 'XBMC.RunPlugin(%s?mode=26&name=%s&url=%s&iconimage=%s&checker=%s)' % (sys.argv[0], name2.lower(), url, iconimage, 'programa')))
        else:
                contextMenuItems.append(('Adicionar programa aos favoritos', 'XBMC.RunPlugin(%s?mode=24&name=%s&url=%s&iconimage=%s&checker=%s)' % (sys.argv[0], name, url, iconimage, 'programa')))
        liz.addContextMenuItems(contextMenuItems, replaceItems=True)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


############################### GOOGLE ANALYTICS XBMC by mickey ->http://www.xbmchub.com/forums/general-python-development/4747-%5Bdev-release%5D-final-google-analytics-your-plugin.html

def parseDate(dateString):
    try:
        return datetime.datetime.fromtimestamp(time.mktime(time.strptime(dateString.encode('utf-8', 'replace'), "%Y-%m-%d %H:%M:%S")))
    except:
        return datetime.datetime.today() - datetime.timedelta(days = 1) #force update


def checkGA():

    secsInHour = 60 * 60
    threshold  = 2 * secsInHour

    now   = datetime.datetime.today()
    prev  = parseDate(ADDON.getSetting('ga_time'))
    delta = now - prev
    nDays = delta.days
    nSecs = delta.seconds

    doUpdate = (nDays > 0) or (nSecs > threshold)
    if not doUpdate:
        return

    ADDON.setSetting('ga_time', str(now).split('.')[0])
    APP_LAUNCH()    
   
                   
def send_request_to_google_analytics(utm_url):
    ua='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
    import urllib2
    try:
        req = urllib2.Request(utm_url, None,
                                    {'User-Agent':ua}
                                     )
        response = urllib2.urlopen(req).read()
    except:
        print ("GA fail: %s" % utm_url)        
    return response
       
def GA(group,name):
        try:
            try:
                from hashlib import md5
            except:
                from md5 import md5
            from random import randint
            import time
            from urllib import unquote, quote
            from os import environ
            from hashlib import sha1
            VISITOR = ADDON.getSetting('ga_visitor')
            utm_gif_location = "http://www.google-analytics.com/__utm.gif"
            if not group=="None":
                    utm_track = utm_gif_location + "?" + \
                            "utmwv=" + VERSION + \
                            "&utmn=" + str(randint(0, 0x7fffffff)) + \
                            "&utmt=" + "event" + \
                            "&utme="+ quote("5("+PATH+"*"+group+"*"+name+")")+\
                            "&utmp=" + quote(PATH) + \
                            "&utmac=" + UATRACK + \
                            "&utmcc=__utma=%s" % ".".join(["1", VISITOR, VISITOR, VISITOR,VISITOR,"2"])
                    try:
                        print "============================ POSTING TRACK EVENT ============================"
                        send_request_to_google_analytics(utm_track)
                    except:
                        print "============================  CANNOT POST TRACK EVENT ============================"
            if name=="None":
                    utm_url = utm_gif_location + "?" + \
                            "utmwv=" + VERSION + \
                            "&utmn=" + str(randint(0, 0x7fffffff)) + \
                            "&utmp=" + quote(PATH) + \
                            "&utmac=" + UATRACK + \
                            "&utmcc=__utma=%s" % ".".join(["1", VISITOR, VISITOR, VISITOR, VISITOR,"2"])
            else:
                if group=="None":
                       utm_url = utm_gif_location + "?" + \
                                "utmwv=" + VERSION + \
                                "&utmn=" + str(randint(0, 0x7fffffff)) + \
                                "&utmp=" + quote(PATH+"/"+name) + \
                                "&utmac=" + UATRACK + \
                                "&utmcc=__utma=%s" % ".".join(["1", VISITOR, VISITOR, VISITOR, VISITOR,"2"])
                else:
                       utm_url = utm_gif_location + "?" + \
                                "utmwv=" + VERSION + \
                                "&utmn=" + str(randint(0, 0x7fffffff)) + \
                                "&utmp=" + quote(PATH+"/"+group+"/"+name) + \
                                "&utmac=" + UATRACK + \
                                "&utmcc=__utma=%s" % ".".join(["1", VISITOR, VISITOR, VISITOR, VISITOR,"2"])
                               
            print "============================ POSTING ANALYTICS ============================"
            send_request_to_google_analytics(utm_url)
           
        except:
            print "================  CANNOT POST TO ANALYTICS  ================"
           
           
def APP_LAUNCH():
        versionNumber = int(xbmc.getInfoLabel("System.BuildVersion" )[0:2])
        if versionNumber < 12:
            if xbmc.getCondVisibility('system.platform.osx'):
                if xbmc.getCondVisibility('system.platform.atv2'):
                    log_path = '/var/mobile/Library/Preferences'
                else:
                    log_path = os.path.join(os.path.expanduser('~'), 'Library/Logs')
            elif xbmc.getCondVisibility('system.platform.ios'):
                log_path = '/var/mobile/Library/Preferences'
            elif xbmc.getCondVisibility('system.platform.windows'):
                log_path = xbmc.translatePath('special://home')
                log = os.path.join(log_path, 'xbmc.log')
                logfile = open(log, 'r').read()
            elif xbmc.getCondVisibility('system.platform.linux'):
                log_path = xbmc.translatePath('special://home/temp')
            else:
                log_path = xbmc.translatePath('special://logpath')
            log = os.path.join(log_path, 'xbmc.log')
            logfile = open(log, 'r').read()
            match=re.compile('Starting XBMC \((.+?) Git:.+?Platform: (.+?)\. Built.+?').findall(logfile)
        elif versionNumber > 11:
            print '======================= more than ===================='
            log_path = xbmc.translatePath('special://logpath')
            log = os.path.join(log_path, 'xbmc.log')
            logfile = open(log, 'r').read()
            match=re.compile('Starting XBMC \((.+?) Git:.+?Platform: (.+?)\. Built.+?').findall(logfile)
        else:
            logfile='Starting XBMC (Unknown Git:.+?Platform: Unknown. Built.+?'
            match=re.compile('Starting XBMC \((.+?) Git:.+?Platform: (.+?)\. Built.+?').findall(logfile)
        print '==========================   '+PATH+' '+VERSION+'  =========================='
        try:
            from hashlib import md5
        except:
            from md5 import md5
        from random import randint
        import time
        from urllib import unquote, quote
        from os import environ
        from hashlib import sha1
        import platform
        VISITOR = ADDON.getSetting('ga_visitor')
        for build, PLATFORM in match:
            if re.search('12',build[0:2],re.IGNORECASE):
                build="Frodo"
            if re.search('11',build[0:2],re.IGNORECASE):
                build="Eden"
            if re.search('13',build[0:2],re.IGNORECASE):
                build="Gotham"
            print build
            print PLATFORM
            utm_gif_location = "http://www.google-analytics.com/__utm.gif"
            utm_track = utm_gif_location + "?" + \
                    "utmwv=" + VERSION + \
                    "&utmn=" + str(randint(0, 0x7fffffff)) + \
                    "&utmt=" + "event" + \
                    "&utme="+ quote("5(APP LAUNCH*"+build+"*"+PLATFORM+")")+\
                    "&utmp=" + quote(PATH) + \
                    "&utmac=" + UATRACK + \
                    "&utmcc=__utma=%s" % ".".join(["1", VISITOR, VISITOR, VISITOR,VISITOR,"2"])
            try:
                print "============================ POSTING APP LAUNCH TRACK EVENT ============================"
                send_request_to_google_analytics(utm_track)
            except:
                print "============================  CANNOT POST APP LAUNCH TRACK EVENT ============================"
checkGA()
             
params=get_params()
url=None
name=None
mode=None
checker=None
iconimage=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
try:        
        checker=urllib.unquote_plus(params["checker"])
except:
        pass
try:        
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Checker: "+str(checker)
print "iconimage: "+str(iconimage)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        print ""+url
        INDEX(url)
       
elif mode==2:
        print ""+url
        VIDEOLINKS(url,name)

elif mode==3:
        print ""
        LIVEMENU()

elif mode==4:
        print ""
        LIVEFUNCTION(url)

elif mode==5:
        print ""
        ONDEMANDMENU()

elif mode==6:
        print ""
        RECOMENDADOS(url)

elif mode==7:
        print ""
        POPULARES(url)

elif mode==8:
        print ""
        RECENTESMENU()

elif mode==9:
        print ""
        RECENTES(url)

elif mode==10:
        print ""
        page_logical='0'
        programa_paginicial(url,page_logical)

elif mode==11:
        print ""
        page_logical='1'
        programa_paginicial(url,page_logical)

elif mode==12:
        print ""
        AZMENU()

elif mode==13:
        print ""
        TVAZMENU()

elif mode==14:
        print ""
        RADIOAZMENU()

elif mode==15:
        print ""
        azfunction(name,url)

elif mode==16:
        print ""
        EMISSAOLISTARMENU()

elif mode==17:
        print ""
        EMISSAOLISTARMENU_CANAL(url)

elif mode==18:
        print ""
        EMISSAOLISTARMENU_TEMA(url)

elif mode==19:
        print ""
        page_logical='0'
        programa_emissoes(url,page_logical)

elif mode==20:
        print ""
        page_logical='1'
        programa_emissoes(url,page_logical)

elif mode==21:
        print ""
        pesquisa_emissoes()

elif mode==22:
        print ""
        pesquisa_programas()

elif mode==23:
        print ""
        play_lista(url,name)

elif mode==24:
        print ""
        ADD_TO_FAVOURITES(name,url,iconimage,checker)

elif mode==25:
        print ""
        FAVORITOS_PROGRAMAS()

elif mode==26:
        print ""
        REMOVER_PROGRAMAS_FAVORITO(name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
