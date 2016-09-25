const path = require('path');

module.exports = {
  entry: './client/js/habit_fantasy.js',
  output: {
    path: path.resolve('./assets'),
    filename: 'bundle.js',
  },
  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        loader: 'babel',
      },
    ],
  },
};
