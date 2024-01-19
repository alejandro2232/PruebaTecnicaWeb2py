// jest.config.js
module.exports = {
    preset: 'ts-jest',
    testEnvironment: 'node',
    roots: ['<rootDir>/ts', '<rootDir>/tests'],
    moduleDirectories: ['node_modules', 'static','ts'],
    transform: {
      '^.+\\.tsx?$': 'ts-jest',
    },
    testRegex: '(/tests/.*\\.test\\.(ts|tsx))$',
    moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx', 'json', 'node'],
    setupFilesAfterEnv: ['jest-fetch-mock'],
    testEnvironment: 'jest-environment-jsdom',
  };
  