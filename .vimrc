""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Author:
"               Moonhead
"
" Version:
"               1.0 - 01/20/2014
"               1.1 - 10/10/2014
"
" Raw_Version:
"               http://pastebin.com/u/Moonhead
"
" Sections:
"               General
"               VIM Interface
"               Colors
"               Undo/Backup/SWP
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 
 
 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                                    General
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 
set nocompatible                        " Vi compatibility!
set history=1000                        " Set how many lines of history
                                        " VIM has to remember
filetype plugin on                      " Enable filetype plugin
set autoread                            " Set auto read when a file is changed
let mapleader=","                       " Extra key combination
nmap <leader>w :w!<cr>                  " Fast saving
set fileformats=unix,dos,mac            " Open files from mac/dos
set exrc                                " Enable per-directory .vimrc files
set secure                              " Disable unsafe commands in .vimrc
syntax on                               " Enable syntax
map <C-J> :next <CR>                    " Switch between files using ctrl + l
map <C-K> :prev <CR>                    " Switch between files using ctrl + h
 
 
 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                                 VIM Interface
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 
 
 
set wildmenu                            " Turn on wild menu
set wildignore=*.o,*~,*.pyc             " Ignored compiled files
set wildmode=list:longest,full          " Auto-completes longest common command
set ruler                               " Always show current position
set showcmd                             " Shows what command you are typing
set cmdheight=2                         " Height of the command bar
set mouse=a                             " Enable mouse usage
set modeline                            " Show what I'm doing
set backspace=eol,start,indent          " Allow backpaces
set ignorecase                          " Ignore case when searching
set hlsearch                            " Highlight search results
set showmatch                           " Display matching brackets
set mat=2                               " Blink when matching brackets
set noerrorbells                        " Turn off error bell sounds
set novisualbell                        " Turn off bell sounds
set t_vb=                               " Disable beeping
set tm=500                              " Disable annoying sounds
set hidden                              " Don't unload buffer
set number                              " Line numbers
set autoindent                          " Autoindent on
set nojoinspaces                        " Don't add random white space
set scrolloff=10                        " 10 lines above and below cursor
set textwidth=80                        " Text width is 80
set bs=2                                " Fix backspacing in insert mode
set smartindent                         " Enable smart indent
set ruler
set cc=80
set shiftwidth=3                        " Enable shift width in 3 spaces
set tabstop=3                           " Tab is 3 spaces
set expandtab                           " Expand the tab
highlight OverLength                           
                \ ctermbg=red           " Over 80 lines
                \ ctermfg=white
                \ guibg=#8F0000
match OverLength /\%81v.\+/             " Match overlength
hi ColorColumn
                \ guibg=#FF0000         " Highlight overlength
                \ ctermbg=246
" bracket auto-completion
" inoremap ( ()<ESC>i
" inoremap [ []<ESC>i
" inoremap { {}<ESC>i
" inoremap < <><ESC>i


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                                    Colors
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 
 
 
"colorscheme jellybeans                 " Jellybean colorscheme
"colorscheme evening                     " Built in colorscheme
 
 
 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                                 Undo/Backup/SWP
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set undofile                            " Undo's file
set undodir=$HOME/.vim/undo             " Need a direcoty in home./vim called undo
set undolevels=1000                     " Maximum number of changes
set undoreload=10000                    " Maximum number lines to save for undo
set noswapfile                          " No swap file
