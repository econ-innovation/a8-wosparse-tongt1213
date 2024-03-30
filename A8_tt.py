import csv

# 文件路径
file_path = 'D://assignment_wosparse/qje2014_2023.txt'

# 初始化存储结构
papers_info = []
abstracts_info = []
titles_info = []
authors_info = []
affiliations_info = []
references_info = []

# 读取文件
with open(file_path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t')
    
    for row in reader:
        # 基本信息提取
        papers_info.append({
            'ut': row['UT'],
            'PY': row['PY'],
            'SO': row['SO'],
            'SN': row['SN'],
            'DI': row['DI'],
            'IS': row['IS'],
            'VL': row['VL']
        })
        
        # 摘要信息提取
        abstracts_info.append({'ut': row['UT'], 'AB': row['AB']})
        
        # 题目信息提取
        titles_info.append({'ut': row['UT'], 'TI': row['TI']})
        
        # 作者信息处理（示例，需要根据具体情况调整）
        # 假设AF字段包含作者全名，以分号分隔
        authors = row['AF'].split('; ')
        for i, author in enumerate(authors):
            authors_info.append({
                'ut': row['UT'],
                'AF': author,
                # 此处省略对family name和given name的拆分
                'order': i + 1
            })
        
        # 参考文献信息处理
        # 假设CR字段包含参考文献，以分号分隔
        references = row['CR'].split('; ')
        for reference in references:
            references_info.append({'ut': row['UT'], 'CR': reference})
            
        # 作者与单位信息提取（示例，需要根据具体情况调整）
        # 此处简化处理，实际可能需要更复杂的逻辑来提取和关联单位信息
        affiliations_info.append({
            'ut': row['UT'],
            'AF': row['AF'],  # 假设AF字段包含作者全名
            # 省略对单位affiliation地址全文的提取和单位署名顺序的处理
        })

# 写入CSV文件的函数
def write_to_csv(file_name, data, field_names):
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)

# 调用函数，将数据写入CSV文件
write_to_csv('papers_info.csv', papers_info, papers_info[0].keys())
write_to_csv('abstracts_info.csv', abstracts_info, abstracts_info[0].keys())
write_to_csv('titles_info.csv', titles_info, titles_info[0].keys())
write_to_csv('authors_info.csv', authors_info, authors_info[0].keys())
write_to_csv('affiliations_info.csv', affiliations_info, affiliations_info[0].keys())
write_to_csv('references_info.csv', references_info, references_info[0].keys())
