//O código vai dentro de um if que verifica se a logo já foi adicionada na página, caso não tenha sido, será feito
let section = parent.document.querySelector('section').children[0]
if(section.children[1].id != 'logo'){
    //Aumentando a visibilidade dos gráficos para 100% da seção lateral direita
    parent.document.querySelectorAll('.block-container')[1].style.minWidth = '100%'

    //Inserindo logo no canto superior direito
    let logoUNIFAN = parent.document.createElement('div')
    logoUNIFAN.innerHTML = '<img src="https://gruponobre.instructure.com/users/180/files/1878/preview?verifier=vFmKXmEezAKtO8gN1UCPPqcdyHKZ7bsfY6zISnB8" width="240px" alt="logo"/>'
    logoUNIFAN.setAttribute('id','logo')
    let children = section.children[1]
    section.insertBefore(logoUNIFAN, children)

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
parent.document.querySelector('.main').style.backgroundImage = 'url("https://gruponobre.instructure.com/users/180/files/1891/preview?verifier=vJn775TlcSDXxQBPh7EkupbY8FrmZHpYqcV9zoEc")'

parent.document.querySelector('header').style.background = 'transparent'

//Centralizando título
let spans = parent.document.querySelectorAll('span')
for(i=0;i<spans.length;i++){
    if(spans[i].textContent.match('UNIFAN')){
        spans[i].style.display = 'flex'
        spans[i].style.justifyContent = 'center'
    }
}

//Adicionando banner na página início
// let bannerDiv = parent.document.querySelectorAll('.block-container')[1].children[0].children[0].children[1]
// if(bannerDiv.children[0].id != 'banner'){
//     let banner = parent.document.createElement('img')
//     banner.style.width = '90%'
//     banner.setAttribute('id','banner')
//     banner.setAttribute('src', 'https://gruponobre.instructure.com/users/180/files/1418/preview?verifier=g1eL9nh61jyhV3rcogLgh9zYlmwdDhpz2awS9qp7')
//     bannerDiv.appendChild(banner)
// }

// bannerDiv.style.marginTop = '-8%'
// bannerDiv.style.display = 'flex'
// bannerDiv.style.flexDirection = 'column'
// bannerDiv.style.alignItems = 'center'

