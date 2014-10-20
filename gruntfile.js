/* To prevent jshint from yelling at module.exports. */
/* jshint node:true */

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
        static_path: 'photowall/static',
        compass: {
            options: {
                sassDir: '<%= static_path %>/sass',
                imagesDir: '<%= static_path %>/imgs',
                cssDir: '<%= static_path %>/css',
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

        cssmin: {
            css: {
                src: '<%= static_path %>/css/style.css',
                dest: '<%= static_path %>/css/style.min.css',
                options: {
                    keepSpecialComments: 0
                }
            }
        },

        // 检查JavaScript语法
        jshint: {
            options: {
                jshintrc: '.jshintrc'
            },
            source: [
                'Gruntfile.js',
                '<%= static_path %>/js/**/*.js',
                '!<%= static_path %>/js/**/*.min.js',
            ]
        },

        uglify: {
            options: {
                //生成一个banner注释并插入到输出文件的顶部
                banner: '/*! <%= pkg.name %> */\n'
            },
            dist: {
                files: {
                    '<%= static_path %>/js/index.min.js': ['<%= static_path %>/js/**/*.js','!<%= static_path %>/js/index.min.js']
                }
            }
        },

        watch: {
            styles: {
                files: [
                    '<%= static_path %>/sass/**/*.scss',
                    '<%= static_path %>/css/**/*.css',
                    '!<%= static_path %>/css/**/*.min.css'
                ],
                tasks: ['compass:uncompressed','cssmin']
            },

            // when scripts change, lint them and copy to destination
            scripts: {
                files: ['<%= static_path %>/js/**/*.js','!<%= static_path %>/js/**/*.min.js'],
                tasks: ['jshint:source','uglify']
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-compass');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Develop task
    grunt.registerTask('develop', 'The default task for developers.\nRuns the tests, builds the minimum required, serves the content (source and destination) and watches for changes.', function() {
        return grunt.task.run([
            'compass:uncompressed',       // Build the CSS using Compass without compression
            'cssmin',
            'jshint:source',
            'uglify',
            'watch'
        ]);

    });

    //下面这个可以在命令行中通过'grunt'来运行默认指定的任务
    grunt.registerTask('default', 'develop');
};
