const { defineConfig } = require('@vue/cli-service')
module.exports = {
    transpileDependencies: true,
    devServer: {
        historyApiFallback: true,
        allowedHosts: "all",
    },
    pwa: {
        name: 'Vue Argon Design',
        themeColor: '#172b4d',
        msTileColor: '#172b4d',
        appleMobileWebAppCapable: 'yes',
        appleMobileWebAppStatusBarStyle: '#172b4d'
    },
    css: {
        // Enable CSS source maps.
        sourceMap: process.env.NODE_ENV !== 'production'
    }
}
