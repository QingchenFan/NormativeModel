import glob
import pandas as pd
# TODO : BN210 拼 BN36
# TODO : 修改路径（HC、MDD），执行两次
path = '/Volumes/QCI/NormativeModel/Data135/MDD/Strufeature_Brainnetom/*/*_GrayVol.csv'
data = glob.glob(path)
for i in data:

    subId = i.split('/')[-2]
    print(subId)

    subcpath ="/Volumes/QCI/NormativeModel/Data135/MDD/Strufeature_Brainnetom/"+subId+"/BN_Atlas_subcotex.txt"


    # 步骤1: 读取BN_Atlas_subcotex.txt文件，并提取Volume_mm3和StructName列
    with open(subcpath, 'r') as file:
        lines = file.readlines()

    # 初始化列表来存储数据
    struct_names = []
    volumes = []

    # 找到数据开始的位置
    data_start = False
    for line in lines:
        if 'ColHeaders' in line:
            data_start = True
            continue
        if data_start and len(line.strip()) > 0:  # 确保跳过空行
            line = line.strip().split()
            if len(line) >= 5:
                struct_names.append(line[4])  # StructName
                volumes.append(float(line[3]))  # Volume_mm3

    # 将数据转换为DataFrame
    volume_struct_df = pd.DataFrame({
        'StructName': struct_names,
        'Volume_mm3': volumes
    })

    # 转置DataFrame，使其成为两行数据
    volume_struct_df_transposed = volume_struct_df.T
    volume_struct_df_transposed = volume_struct_df_transposed.reset_index(drop=True)
    # volume_struct_df_transposed = pd.DataFrame(volume_struct_df_transposed)
    print(volume_struct_df_transposed)
    # 步骤2: 读取sub-HC001_GrayVol.csv文件
    gray_vol_df = pd.read_csv(i)
    print(gray_vol_df)
    # 步骤3: 将转置后的Volume_mm3和StructName两行添加到sub-HC001_GrayVol.csv文件的DataFrame中
    # 由于只需要添加两行，我们可以直接使用concat函数，并通过ignore_index重新设置索引
    result_df = pd.concat([gray_vol_df, volume_struct_df_transposed], axis=1)

    # 保存新的CSV文件
    result_df.to_csv('/Volumes/QCI/NormativeModel/Data135/MDD/Strufeature_Brainnetom/'+subId+'/'+subId+'_GrayVolSubcortical.csv', index=False)


