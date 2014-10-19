'use strict';

module.exports = function(grunt) {
    // 在这里配置你的grunt任务
    // jshint（检查语法错误）、concat（合并文件）、uglify（压缩代码）和watch（自动执行）


    // grunt-contrib-clean：删除文件。
    // grunt-contrib-compass：使用compass编译sass文件。
    // grunt-contrib-concat：合并文件。
    // grunt-contrib-copy：复制文件。
    // grunt-contrib-cssmin：压缩以及合并CSS文件。
    // grunt-contrib-imagemin：图像压缩模块。
    // grunt-contrib-jshint：检查JavaScript语法。
    // grunt-contrib-uglify：压缩以及合并JavaScript文件。
    // grunt-contrib-watch：监视文件变动，做出相应动作。

    grunt.initConfig({
        // 从package.json文件中读取我们的项目配置并存储到pkg属性中
        pkg: grunt.file.readJSON('package.json'),
        compass: {
            options: {
                sassDir: 'photowall/static/sass',
                imagesDir: 'photowall/static/imgs',
                cssDir: 'photowall/static/css',
                force: true
            },
            uncompressed: {
                options: {
                    outputStyle: 'expanded'
                }
            },
            compressed: {
                options: {
                    outputStyle: 'compressed'
                }
            }
        },

        jshint: {
            options: {
                jshintrc: '.jshintrc'
            },
            source: [
                'Gruntfile.js',
                'photowall/static/js/**/*.js',
                'photowall/static/js/**/*.min.js'
            ]
        },

        uglify: {
            options: {
                //生成一个banner注释并插入到输出文件的顶部
                banner: '/*! <%= pkg.name %> */\n'
            },
            dist: {
                files: {
                    'photowall/static/js/index.min.js': ['photowall/static/js/*.js']
                }
            }
        },

        watch: {
            styles: {
                files: [
                    'photowall/static/sass/*.scss',
                ],
                tasks: ['compass:compressed']
            },

            // when scripts change, lint them and copy to destination
            scripts: {
                files: ['photowall/static/js/*.js'],
                tasks: ['uglify']
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-compass');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Develop task
    grunt.registerTask('develop', 'The default task for developers.\nRuns the tests, builds the minimum required, serves the content (source and destination) and watches for changes.', function() {
        return grunt.task.run([
            'compass:compressed',       // Build the CSS using Compass without compression
            'uglify',
            'watch'
        ]);

    });

    //下面这个可以在命令行中通过'grunt'来运行默认指定的任务
    grunt.registerTask('default', 'develop');
};
