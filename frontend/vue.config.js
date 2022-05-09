module.exports = {
  devServer: {
    allowedHosts: "all",
    watchFiles: {
      paths: ["src/**/*", "public/**/*"],
      options: {
        usePolling: true,
      },
    },
  },
};
