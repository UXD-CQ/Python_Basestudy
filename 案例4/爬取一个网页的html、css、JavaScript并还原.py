import asyncio
from pyppeteer import launch

async def main():
    # 启动浏览器
    browser = await launch()
    # 打开一个新页面
    page = await browser.newPage()
    # 跳转到目标网页
    await page.goto('https://example.com')
    # 等待页面加载完成
    await page.waitForLoadState('networkidle2')

    # 获取HTML
    html = await page.content()

    # 获取CSS
    css = await page.evaluate('''() => {
        const styleSheets = document.styleSheets;
        return styleSheets.map(sheet => sheet.href).join('\n');
    }''')

    # 获取JavaScript
    js = await page.evaluate('''() => {
        const scripts = document.scripts;
        return scripts.map(script => script.src).join('\n');
    }''')

    # 打印结果
    print('HTML:')
    print(html)
    print('CSS:')
    print(css)
    print('JavaScript:')
    print(js)

    # 关闭浏览器
    await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
