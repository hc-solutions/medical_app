const { defineConfig } = require('@vue/cli-service')
module.exports = {
  transpileDependencies: true,
  devServer: {
        historyApiFallback: true,
        allowedHosts: "all",
  }
}
