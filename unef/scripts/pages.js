//Parte do código de alinhamento e background é trazido da página "início", se o usuário atualizar uma página ou acessar o link diretamente (professores,coordenadores, etc) sem passar pela tela "início", o código supracitado não terá efeito, por isto o bloco de código abaixo faz uma verificação se as atualizações já foram realizadas ou não por meio da logo gera.
let section = parent.document.querySelector('section').children[0]
if(section.children[1].id != 'logo'){
    //Aumentando a visibilidade dos gráficos para 100% da seção lateral direita
    parent.document.querySelectorAll('.block-container')[1].style.minWidth = '100%'

    //Inserindo logo no canto superior direito
    let logoUNEF = parent.document.createElement('div')
    logoUNEF.innerHTML = '<img src="https://gruponobre.instructure.com/users/180/files/1868/preview?verifier=1sKXIuIockqTa0SaeANhkBvuc6wYnQdj28zt1gRg" alt="logo"/>'
    logoUNEF.setAttribute('id','logo')
    let children = section.children[1]
    section.insertBefore(logoUNEF, children)

    //Centralizando a logo
    let logo = parent.document.querySelector('#logo').style
    logo.paddingTop = '15%'
    logo.display = 'flex'
    logo.justifyContent = 'center'

     //Centralizando o footer
     let footer = parent.document.querySelector('footer')
     footer.style.display = 'flex'
     footer.style.justifyContent = 'center'
     footer.style.gap = '3px'
}

//Adicionando fundo na seção da direita
parent.document.querySelector('.main').style.backgroundImage = 'url("https://gruponobre.instructure.com/users/180/files/1314/preview?verifier=bHe9FOzKxCifF3ip1UsH3cXuyT2JD2bGbBgdm1Yi")'

parent.document.querySelector('header').style.backgroundImage = 'url("https://gruponobre.instructure.com/users/180/files/1314/preview?verifier=bHe9FOzKxCifF3ip1UsH3cXuyT2JD2bGbBgdm1Yi")'


//Alterando o tamanho, colocando borda, sombreamento e alinhando a div de percentuais gerais
let porcentagens = parent.document.querySelectorAll('.block-container')[1].children[0].children[0].children[1]
for(i=0;i<5;i++){
    porcentagens.children[i].children[0].children[0].children[0].children[0].style.display = 'flex'
    porcentagens.children[i].children[0].children[0].children[0].children[0].style.flexDirection = 'column'
    porcentagens.children[i].children[0].children[0].children[0].children[0].style.alignItems = 'center'
    porcentagens.children[i].children[0].children[0].children[0].children[0].style.padding = '50px'
    porcentagens.children[i].children[0].children[0].children[0].children[0].style.border = '1px solid #111'
    porcentagens.children[i].children[0].children[0].children[0].children[0].style.boxShadow = '0 0 3px 1px #11111180'
    porcentagens.children[i].children[0].children[0].children[0].children[0].style.borderRadius = '2px'
    porcentagens.children[i].children[0].children[0].children[0].children[0].children[0].style.fontSize = '20px'
    // porcentagens.children[i].children[0].children[0].children[0].children[0].children[1].style.fontSize = '45px'
}

//Alterando o tamanho e alinhando o título das divs
for(i=0;i<7;i = i + 2){
    parent.document.querySelectorAll('.block-container')[1].children[0].children[0].children[i].style.textAlign = 'center'
    parent.document.querySelectorAll('.block-container')[1].children[0].children[0].children[i].children[0].children[0].children[0].style.fontSize = '35px'
    if(i>0){
        parent.document.querySelectorAll('.block-container')[1].children[0].children[0].children[i].style.marginTop = '2%'
    }
}