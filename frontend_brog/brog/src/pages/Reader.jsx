/**@jsxImportSource @emotion/react */

import ReactDom from "react-dom";
import debounce from "lodash.debounce";
import "../css/reader.css"
import "../css/border.css"
import { useEffect, useState, useRef, useMemo } from "react"

import { css, jsx } from '@emotion/react'

import pdfjsWorker from 'pdfjs-dist/build/pdf.worker.entry';
import * as PDFJS from 'pdfjs-dist/webpack';

import { TextLayerBuilder, EventBus } from "pdfjs-dist/web/pdf_viewer";
import "pdfjs-dist/web/pdf_viewer.css";

PDFJS.GlobalWorkerOptions.workerSrc = pdfjsWorker

const pageChange = 200;

function TestSideEffect() {
    const [ dep, setDep ] = useState( 0 )
    useEffect( () => {
        console.log( 'init !' )
    }, [ dep ] )
    const handleClk = () => setDep( dep => dep + 1 )
    return <div
        onClick={handleClk}
        children={dep}
    />
}

// 写出并调试单页pdf加载器, 用函数式写法
function UniViewer( { pageProxy, width, setSearchContent, setWidth, setisSearch } ) {
    // 获取viewport
    const viewport = pageProxy.getViewport( { scale: 4.0 } )
    // 注意宽度变换时的渲染情况
    const style = css`
        width: ${ width }px;
        height: ${ viewport.height / viewport.width * width }px;
        z-index: 0;
        position: relative;
    `
    // pageRef 在初始化时将被初始化为FiberNode
    const [ pageRef, setPageRef ] = useState( null )
    // pdf.js 插件的事件处理器
    const eventBus = new EventBus()
    // 渲染图形层和文字层, 保证渲染只在pageProxy变化时进行
    // 此时pageRef一定不为空, 才进行下一步
    useEffect( () => {
        // 如果没有pageRef, 后面的init就不会执行
        // 这样就拦下了pageRef是null的情况
        pageRef && init()
        return () => { }
    }, [ pageRef ] )
    async function init() {
        // 通过 eventBus 
        const div = document.createElement( 'div' )
        div.setAttribute( "id", "page-" + ( pageProxy.pageIndex + 1 ) )
        // 渲染canvas层
        let canvas = document.createElement( "canvas" )
        div.append( canvas )
        let context = canvas.getContext( '2d' )
        canvas.height = viewport.height
        canvas.width = viewport.width
        canvas.setAttribute( 'style', `
            width: ${ width }px;
            height: ${ viewport.height / viewport.width * width }px;
            z-index: 0;
        `)
        await pageProxy.render( {
            canvasContext: context,
            viewport: viewport
        } )
        // 等待渲染完成后, 再获取文字层信息 ( 否则获取不到 )
        let textContent = await pageProxy.getTextContent()
        // 添加新元素作为文字层的容器
        let textLayerDiv = document.createElement( "div" )
        textLayerDiv.setAttribute( "class", "textLayer" );
        textLayerDiv.setAttribute( "style", `
            z-index: 1;
        `)


        //选中监听
        let s_content = '';
        let div_selection = document.createElement('div');
        div_selection.setAttribute("class", "div_selection")
        let newContent = document.createTextNode("搜索");
        div_selection.appendChild(newContent);
        div_selection.onclick = ()=>{
            console.log(1111)
            // setWidth( ( width ) => ( width - pageChange ) );
            setisSearch(()=>1);
            setSearchContent(()=>s_content);
            div_selection.setAttribute("style",`
                display:none;
            `);
        }
        pageRef.appendChild(div_selection)
        const mouse_up_watch = (e)=>{
            if (window.getSelection().toString() != "")
            {console.log(window.getSelection().toString());
            s_content = window.getSelection().toString();
            }
        }
        textLayerDiv.addEventListener('mouseup', mouse_up_watch);
        textLayerDiv.oncontextmenu = (e)=>{
            e.preventDefault();
            let xx = textLayerDiv.getBoundingClientRect().x
            let yy = textLayerDiv.getBoundingClientRect().y
            div_selection.setAttribute("style",`
                display:flex;
                top:${e.pageY-yy + 'px'};
                left:${e.pageX-xx + 'px'};
            `);
        }
        textLayerDiv.onclick = ()=>{
            div_selection.setAttribute("style",`
                display:none;
            `);
        }
        ///test



        div.append( textLayerDiv )
        // 将文字层渲染到容器
        const smallviewport = pageProxy.getViewport( {
            scale: width / viewport.width * 4.0
        } )
        let textLayer = new TextLayerBuilder( {
            textLayerDiv: textLayerDiv,
            pageIndex: pageProxy.pageIndex,
            viewport: smallviewport,
            eventBus: eventBus
        } )
        textLayer.setTextContent( textContent )
        textLayer.render()
        // 渲染pdf上的标记 ( 未实现 )
        console.log( await pageProxy.getAnnotations() )
        // 最后将div提交给FiberNode
        pageRef.appendChild( div )
    }
    // 当宽度出现变化时, 重新渲染文字层, 并改变图片层的样式
    useEffect( () => {
        pageRef && modifyWidth()
        return () => { }
    }, [ width ] )
    async function modifyWidth() {
        // 改变图片层的样式, 使得它对应width放大或缩小
        const [ canvas ] = pageRef.getElementsByTagName( 'canvas' )
        canvas.setAttribute( 'style', `
            width: ${ width }px;
            height: ${ viewport.height / viewport.width * width }px;
            z-index: 0;
        `)
        // 重新渲染文字层
        const [ textLayerDiv ] = pageRef.getElementsByClassName( 'textLayer' )
        textLayerDiv.innerHTML = ''
        let textContent = await pageProxy.getTextContent()
        const smallviewport = pageProxy.getViewport( {
            scale: width / viewport.width * 4.0
        } )
        let textLayer = new TextLayerBuilder( {
            textLayerDiv: textLayerDiv,
            pageIndex: pageProxy.pageIndex,
            viewport: smallviewport,
            eventBus: eventBus
        } )
        textLayer.setTextContent( textContent )
        textLayer.render()
    }
    // 注意从react 17开始获得的节点就是fiberNode了
    return <div
        // highlight应该由父组件管理并改变子组件状态, 因为单次选择可能跨页
        // highlight={?}
        css={style}
        className={`uni-viewer-page-${ pageProxy._pageIndex + 1 } position_uni`}
        key={`uni-viewer-page-${ pageProxy._pageIndex + 1 }`}
        ref={( fiberNode ) => { fiberNode && setPageRef( fiberNode ) }}
    />
}

function TestUniViewer({setisSearch,setSearchContent}) {
    const [ pageProxy, setPageProxy ] = useState()
    const [ width, setWidth ] = useState( 900 )
    const url = 'https://arxiv.org/pdf/1601.00670.pdf'
    // const url = "../src/testpdf/Introduction to algorithms by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein (z-lib.org).pdf"
    // 当dependency中的内容出现变化时, useEffect才会执行
    // dependency中没有内容, 就只在初次加载时执行
    useEffect( () => {
        init()
        return () => { }
    }, [] )
    async function init() {
        const pdfLoader = await PDFJS.getDocument( url )
        setPageProxy( await ( await pdfLoader.promise ).getPage( 1 ) )
    }
    const mo = ()=>{
        console.log(window.getSelection());
    }
    return ( pageProxy ?
        <div>
            {/* <button
                onClick={() => { setWidth( ( width ) => ( width + 100 ) ) }}
                css={css`width: 100px; height: 100px;`}
                children={<p>bigger</p>}
            />
            <button
                onClick={() => { setWidth( ( width ) => ( width - 100 ) ) }}
                css={css`width: 100px; height: 100px;`}
                children={<p>smaller</p>}
            /> */}
            <UniViewer setSearchContent={setSearchContent} setisSearch={setisSearch} pageProxy={pageProxy}  setWidth={setWidth} width={width} />
        </div>
        : <div> Loading </div>
    )
}

function MultiViewer( { pdfProxy, scale } ) {
    const [ page, setPage ] = useState( 100 )
    const [ content, setContent ] = useState( [] )

    const style = css`
        overflow: scroll;
        height: 300px;
        background-color: yellow;
        display: block;
    `

    const onscroll = ( e ) => {
        console.log( e )
        setPage( page => page + 1 )
    }

    useEffect( () => () => {
        console.log( content )
        content.push( <tr> abcd </tr> )
        setContent( content )
    }, [ page ] )

    useEffect( () => () => {
        for ( let i = 0; i < 100; ++i )
            content.push( <tr> abcd </tr> )
        setContent( content )
    }, [ page ] )

    console.log( content )

    return (
        <div className={'abcd'} css={style} onScroll={onscroll}>
            {content}
        </div>
    )
}

function TestMultiViewer() {
    const [ pdfProxy, setPdfProxy ] = useState()
    const url = './testpdf/Introduction to algorithms by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein (z-lib.org).pdf'
    // const url = 'https://arxiv.org/pdf/1601.00670.pdf'
    // 当dependency中的内容出现变化时, useEffect才会执行
    // dependency中没有内容, 就只在初次加载时执行
    useEffect( () => {
        init()
        return () => { }
    }, [] )

    async function init() {
        const pdfLoader = await PDFJS.getDocument( url )
        setPdfProxy( await ( await pdfLoader.promise ) )
    }

    return pdfProxy ?
        <MultiViewer pdfProxy={pdfProxy} scale={4.0} />
        : <div> Loading </div>
}


function Reader() {
    let [bookName, setbookName] = useState("代数学方法（第一卷）");
    let [isSearch, setisSearch] = useState(0);
    let [searchContent, setSearchContent] = useState('');
    useEffect(()=>{
        console.log(isSearch);
    }, [isSearch])
    return (
        <div className = {"reader_box"}>
            <div className = {"viewer_box top_bottom_border"}>
                <div className = {"name_title"}>
                    {bookName}
                </div>
                <hr className = {"hr_style"}></hr>
                <TestUniViewer setisSearch={setisSearch} setSearchContent={setSearchContent} />
            </div>
            {isSearch ? 
            <div className={"search_ret top_bottom_border"}>
                <h1 className={"search_title"}>搜索结果</h1>
                <hr className="hr_style"></hr>
                <div className={"search_content"}>
                    {searchContent}
                </div>
            </div>:<div></div>}
        </div>
    )
}

export default Reader;
