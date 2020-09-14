"NeoBundle Scripts-----------------------------
if &compatible
  set nocompatible               " Be iMproved
endif

" Required:
set runtimepath+=/home/colin/.vim/bundle/neobundle.vim/

" Required:
call neobundle#begin(expand('/home/colin/.vim/bundle'))

" Let NeoBundle manage NeoBundle
" Required:
NeoBundleFetch 'Shougo/neobundle.vim'

" Add or remove your Bundles here:
NeoBundle 'Shougo/neosnippet.vim'
NeoBundle 'Shougo/neosnippet-snippets'
NeoBundle 'tpope/vim-fugitive'
NeoBundle 'ctrlpvim/ctrlp.vim'
NeoBundle 'flazz/vim-colorschemes'
NeoBundle 'Dave-Elec/gruvbox' 			"colorscheme
"NeoBundle 'Yggdroot/indentLine' 		"indent lines
NeoBundle 'vim-airline/vim-airline' 		"status bar
NeoBundle 'tpope/vim-fugitive' 			"git wrapper
NeoBundle 'preservim/nerdtree'			"tree navigation
"NeoBundle 'ycm-core/YouCompleteMe' 		"code autocomplete
"NeoBundle 'vim-syntastic/syntastic' 		"syntax checker
NeoBundle 'tpope/vim-surround'			"surroundings 

" You can specify revision/branch/tag.
NeoBundle 'Shougo/vimshell', { 'rev' : '3787e5' }

" Required:
call neobundle#end()

" Required:
filetype plugin indent on

" If there are uninstalled bundles found on startup,
" this will conveniently prompt you to install them.
NeoBundleCheck
"End NeoBundle Scripts-------------------------

" Gruvbox setup
let g:gruvbox_contrast_dark = 'hard'
let g:gruvbox_transparent_bg=1
autocmd vimenter * colorscheme gruvbox
set background=dark
set termguicolors

" Airline Config settings
let g:airline_powerline_fonts = 1
let g:airline#extensions#tabline#enabled = 1
let g:airline_theme = 'gruvbox'
autocmd VimEnter * AirlineRefresh

" Syntastic Config settigns
"set statusline+=%#warningmsg#
"set statusline+=%{SyntasticStatuslineFlag()}
"set statusline+=%*
"let g:syntastic_always_populate_loc_list = 1
"let g:syntastic_auto_loc_list = 1
"let g:syntastic_check_on_open = 1
"let g:syntastic_check_on_wq = 0

" convenience
syntax enable
set number
set ruler
set cursorline
set showmatch
set wildmenu
let g:indentLine_char = '▏'

" indentation/whitespaces
set autoindent
set smartindent
set shiftwidth=4

" searching
set hlsearch
set incsearch
set ignorecase
set smartcase

" remaps
nnoremap j gj
nnoremap k gk
map <C-n> :NERDTreeToggle<CR>
nnoremap x "_x
nnoremap d "_d
nnoremap D "_D
vnoremap d "_d
map <C-h> <C-W>h
map <C-j> <C-W>j
map <C-k> <C-W>k
map <C-l> <C-W>l

