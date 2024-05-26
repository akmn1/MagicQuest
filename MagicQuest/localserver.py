# 这个模块包含了部署本地服务的代码,并提供了三个函数用来上传文件,上传压缩文件和下载文件.服务在本地端口部署
from flask import Flask, request, send_from_directory, jsonify
import os
import zipfile
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)


# UPLOAD_DIRECTORY = os.path.join(PROJECT_ROOT, 'DB','background_resources')
UPLOAD_DIRECTORY = r"E:\testresources"
@app.route("/upload", methods=["POST"])
def upload_file():
    """处理文件上传"""
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file:
        filename = file.filename
        file.save(os.path.join(UPLOAD_DIRECTORY, filename))
        return f"{filename} uploaded successfully", 200
@app.route("/upload-folder", methods=["POST"])
def upload_folder():
    """处理文件夹（打包为zip文件）的上传"""
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    new_filename = request.form.get('filename')  # 获取额外的文件名参数
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and file.filename.endswith('.zip'):
        os.makedirs(fr'{UPLOAD_DIRECTORY}/{new_filename}')
        UPLOADFILE=fr'{UPLOAD_DIRECTORY}/{new_filename}'
        filename = file.filename
        file_path = os.path.join(UPLOADFILE, filename)
        file.save(file_path)
        # 解压zip文件，这里不更改内部文件的名称，仅更改zip文件的保存名称
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            for name in zip_ref.namelist():
                re_name = name.encode('cp437').decode('gbk')
                zip_ref.extract(name, UPLOADFILE)
                os.rename(fr'{UPLOADFILE}/{name}', fr'{UPLOADFILE}/{re_name}')

        # 可选：解压后删除zip文件
        # os.remove(file_path)
        return jsonify({"message": f"{filename} uploaded and extracted successfully"}), 200
    else:
        return jsonify({"error": "Unsupported file type"}), 400
@app.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    """处理文件下载"""
    return send_from_directory(UPLOAD_DIRECTORY, filename, as_attachment=True)

if __name__ == "__main__":
    # 确保UPLOAD_DIRECTORY路径存在
    if not os.path.exists(UPLOAD_DIRECTORY):
        os.makedirs(UPLOAD_DIRECTORY)
    app.run(debug=False, port=5000)
