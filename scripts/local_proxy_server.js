const http = require('http');
const httpProxy = require('http-proxy');
const {parse} = require('url');

const proxy = httpProxy.createProxyServer({changeOrigin: true});
const port = 80; // 代理服务器的端口号

const server = http.createServer((req, res) => {
    const {pathname} = parse(req.url);
    // 处理所有请求
    // if (pathname.startsWith('/think-tool-kit')) {
    //     let targetPath = pathname.replace('/think-tool-kit', '');
    //     let targetUrl = `http://127.0.0.1:8080${targetPath}`
    //     console.log(`Proxy to ${targetUrl}`);
    //     req.url = targetUrl;
    //     proxy.web(req, res, {
    //         target: 'http://127.0.0.1:8080',
    //         // target: targetUrl,
    //         // pathRewrite: {'^/think-tool-kit/': '/'},
    //         // changeOrigin: true
    //     }, (err) => {
    //         console.error(err);
    //         res.writeHead(404);
    //         res.end('Oops, something went wrong on the server!');
    //     });
    // } else
    if (pathname.startsWith('/')) {
        // http-server使用的是req.url，所以需要修改这个
        if (pathname.startsWith('/think-tool-kit')) {
            req.url = req.url.replace('/think-tool-kit', '');
        }
        proxy.web(req, res, {target: 'http://127.0.0.1:8080'}, (err) => {
            console.error(err);
            res.writeHead(404);
            res.end('Oops, something went wrong on the server!');
        });
    }
    // 处理其他情况
    else {
        res.writeHead(404);
        res.end('404 Not Found');
    }
});

console.log(`Proxy server running at http://localhost:${port}`);
server.listen(port);
