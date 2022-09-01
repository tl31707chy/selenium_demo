import configparser
import project_conf


class ReadIni:

    def __init__(self):
        """初始化"""
        self.config = configparser.ConfigParser()
        self.config.read(project_conf.ini_path)

    def get_option(self, section, option):
        """
        获取配置文件里数据
        @param section: section--》environment
        @param option: option--》online
        @return:
        """
        return self.config.get(section, option)

    def get_section(self, section):
        """
        获取整个section下的数据
        @param section: environment
        @return:result
        """
        result = {}
        for i in self.config.items(section):
            result[i[0]] = i[1]
        return result


if __name__ == '__main__':
    test = ReadIni()
    print(test.get_option('project', 'url'))
    # print(test.get_section('project'))
